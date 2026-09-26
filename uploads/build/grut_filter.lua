-- grut_filter.lua — pandoc Lua filter for the GRUT public-record PDF.
-- Conversion only: no wording is added or removed. It
--   (1) lifts the leading H1/H2 into title/subtitle metadata,
--   (2) moves the "Abstract" section into the abstract metadata field,
--   (3) typesets the few Unicode math symbols that occur in running text
--       (outside $...$) as LaTeX math, so the Latin Modern text font is
--       never asked for a glyph it lacks (Greek, hbar, arrows, relations).

local SYMBOLS = {
  ["ℏ"] = "\\hbar", ["→"] = "\\rightarrow", ["≡"] = "\\equiv",
  ["×"] = "\\times", ["−"] = "-", ["≥"] = "\\geq", ["≤"] = "\\leq",
  ["ξ"] = "\\xi", ["ε"] = "\\varepsilon", ["Λ"] = "\\Lambda",
  ["ρ"] = "\\rho", ["α"] = "\\alpha", ["μ"] = "\\mu", ["ω"] = "\\omega",
  ["κ"] = "\\kappa", ["τ"] = "\\tau", ["λ"] = "\\lambda", ["ν"] = "\\nu",
  ["π"] = "\\pi", ["ε"] = "\\varepsilon", ["Δ"] = "\\Delta", ["σ"] = "\\sigma",
  ["⁷"] = "^{7}", ["₄"] = "_{4}", ["²"] = "^{2}",
  ["≈"] = "\\approx", ["⟺"] = "\\Longleftrightarrow", ["↦"] = "\\mapsto",
  ["′"] = "^{\\prime}", ["𝔄"] = "\\mathfrak{A}",
}

local function split_str(text)
  -- returns a list of inlines: Str runs and Math pieces
  local out, buf = {}, {}
  local function flush()
    if #buf > 0 then table.insert(out, pandoc.Str(table.concat(buf))); buf = {} end
  end
  for _, cp in utf8.codes(text) do
    local ch = utf8.char(cp)
    local tex = SYMBOLS[ch]
    if tex then
      flush()
      table.insert(out, pandoc.Math("InlineMath", tex))
    else
      table.insert(buf, ch)
    end
  end
  flush()
  return out
end

local function Str(el)
  for ch, _ in pairs(SYMBOLS) do
    if el.text:find(ch, 1, true) then
      return split_str(el.text)
    end
  end
  return nil
end

-- (4) use the vector (PDF) version of a figure when one sits beside the PNG
local function Image(el)
  local pdf = el.src:gsub("%.png$", ".pdf")
  if pdf == el.src then return nil end
  local dirs = { "." }
  for _, d in ipairs(PANDOC_STATE.resource_path or {}) do table.insert(dirs, d) end
  for _, d in ipairs(dirs) do
    local f = io.open(d .. "/" .. pdf, "r")
    if f then f:close(); el.src = pdf; return el end
  end
  return nil
end

local function Pandoc(doc)
  local blocks = doc.blocks
  local meta = doc.meta
  local out = {}
  local i = 1
  -- (1) title / subtitle from the leading headers
  if blocks[1] and blocks[1].t == "Header" and blocks[1].level == 1 then
    meta.title = pandoc.MetaInlines(blocks[1].content); i = 2
    if blocks[2] and blocks[2].t == "Header" and blocks[2].level == 2 then
      meta.subtitle = pandoc.MetaInlines(blocks[2].content); i = 3
    end
  end
  -- (2) abstract section -> metadata
  local abstract = nil
  while i <= #blocks do
    local b = blocks[i]
    if b.t == "Header" and b.level == 2 and pandoc.utils.stringify(b.content) == "Abstract" then
      abstract = {}
      i = i + 1
      while i <= #blocks do
        local c = blocks[i]
        if (c.t == "Header" and c.level <= 2) or c.t == "HorizontalRule" then break end
        table.insert(abstract, c); i = i + 1
      end
    else
      table.insert(out, b); i = i + 1
    end
  end
  if abstract then meta.abstract = pandoc.MetaBlocks(abstract) end
  doc.blocks = out
  doc.meta = meta
  return doc
end

-- (4) inline code (commit hashes, paths, verdict strings) -> breakable \path
local function Code(el)
  if FORMAT:match("latex") then
    local delim = "|"
    for _, d in ipairs({"|", "!", "+", "="}) do
      if not el.text:find(d, 1, true) then delim = d; break end
    end
    return pandoc.RawInline("latex", "\\path" .. delim .. el.text .. delim)
  end
end

-- symbol pass runs first on the whole document, then the structural pass
return {
  { Str = Str, Code = Code, Image = Image },
  { Pandoc = Pandoc },
}
