// make_pdf.mjs — typeset the GRUT public-record Markdown into a print-ready PDF.
//
// Conversion only: no scientific content is generated or altered here; the
// Markdown file is the single source of truth. Math ($...$, $$...$$) is
// rendered with KaTeX; layout is A4 with running header and page numbers.
//
// Usage (from uploads/build):
//   npm install          # katex, markdown-it, markdown-it-texmath, playwright-core
//   node make_pdf.mjs ../GRUT_Consolidated_Theory_PUBLIC_RECORD.md \
//                     ../GRUT_Consolidated_Theory_PUBLIC_RECORD.pdf
// Set CHROMIUM=/path/to/chrome if Chromium is not at the default location.

import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath, pathToFileURL } from 'node:url'
import MarkdownIt from 'markdown-it'
import texmath from 'markdown-it-texmath'
import katex from 'katex'
import { chromium } from 'playwright-core'

const HERE = path.dirname(fileURLToPath(import.meta.url))
const [src, out] = process.argv.slice(2)
if (!src || !out) {
  console.error('usage: node make_pdf.mjs <input.md> <output.pdf>')
  process.exit(2)
}

const md = new MarkdownIt({ html: false, linkify: true, typographer: false })
  .use(texmath, { engine: katex, delimiters: 'dollars', katexOptions: { throwOnError: true, strict: 'ignore' } })

const source = fs.readFileSync(src, 'utf8')
let body
try {
  body = md.render(source)
} catch (e) {
  console.error('MATH RENDER ERROR:', e.message)
  process.exit(1)
}
// any KaTeX error spans left in output are treated as build failures
if (body.includes('katex-error')) {
  const m = body.match(/<span class="katex-error"[^>]*title="([^"]*)"/)
  console.error('KaTeX error in output:', m ? m[1] : '(unknown)')
  process.exit(1)
}
const leftover = body.replace(/<[^>]+>/g, '').match(/\$[^$\n]{1,60}\$/g)
if (leftover) console.warn('WARNING: possible unrendered math:', leftover.slice(0, 5))

const katexCss = pathToFileURL(path.join(HERE, 'node_modules/katex/dist/katex.min.css')).href
const html = `<!doctype html><html><head><meta charset="utf-8">
<title>GRUT — Consolidated Theory (Public Record)</title>
<link rel="stylesheet" href="${katexCss}">
<style>
  @page { size: A4; margin: 22mm 20mm 20mm 20mm; }
  html { font-size: 10.2pt; }
  body { font-family: 'DejaVu Serif', 'Liberation Serif', serif; line-height: 1.45; color: #111; }
  h1 { font-size: 1.55em; margin: 1.6em 0 0.5em; border-bottom: 1px solid #999; padding-bottom: 0.15em; page-break-after: avoid; }
  h1:first-of-type { font-size: 2.0em; border: none; margin-top: 0; text-align: center; }
  h1:first-of-type + h2 { text-align: center; font-weight: normal; font-style: italic; margin-top: 0; }
  h2 { font-size: 1.22em; margin: 1.3em 0 0.4em; page-break-after: avoid; }
  h3 { font-size: 1.05em; margin: 1.1em 0 0.3em; page-break-after: avoid; }
  p, li { text-align: justify; hyphens: auto; }
  blockquote { margin: 0.8em 1.2em; padding: 0.4em 0.9em; border-left: 3px solid #555; background: #f4f4f4; }
  table { border-collapse: collapse; width: 100%; margin: 0.7em 0; font-size: 0.86em; page-break-inside: auto; }
  tr { page-break-inside: avoid; }
  th, td { border: 1px solid #999; padding: 3px 5px; vertical-align: top; text-align: left; }
  th { background: #e6e6e6; }
  code { font-family: 'DejaVu Sans Mono', monospace; font-size: 0.86em; word-break: break-all; }
  hr { border: none; border-top: 1px solid #bbb; margin: 1.4em 0; }
  .katex-display { margin: 0.7em 0; overflow-x: hidden; }
  .katex { font-size: 1.05em; }
</style></head><body>${body}</body></html>`

const tmpHtml = path.join(HERE, '_render.html')
fs.writeFileSync(tmpHtml, html)

const exe = process.env.CHROMIUM || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
const browser = await chromium.launch({ executablePath: exe })
const page = await browser.newPage()
await page.goto(pathToFileURL(tmpHtml).href, { waitUntil: 'networkidle' })
await page.pdf({
  path: out,
  format: 'A4',
  printBackground: true,
  displayHeaderFooter: true,
  margin: { top: '22mm', bottom: '20mm', left: '20mm', right: '20mm' },
  headerTemplate: `<div style="font-size:7.5pt;width:100%;padding:0 20mm;color:#555;font-family:serif;">
    <span>GRUT — Consolidated Theory · Public Record (source boundary 25 Sep 2026)</span></div>`,
  footerTemplate: `<div style="font-size:7.5pt;width:100%;text-align:center;color:#555;font-family:serif;">
    D. Ryan Grover · page <span class="pageNumber"></span> of <span class="totalPages"></span></div>`,
})
await browser.close()
fs.unlinkSync(tmpHtml)
console.log('wrote', out)
