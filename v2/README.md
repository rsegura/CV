# Roberto Segura - personal website v2

Four static pages: About, Experience, Projects, Learning. Open index.html directly or serve the parent folder and visit /v2/.

The original ../index.html is preserved. Shared styling is in assets/style.css. No JavaScript or external runtime is required.

build.py regenerates the four pages using the approved content from ../index.html. build_pdf.py generates the curated two-page CV with ReportLab and copies it to ../output/pdf/.

Checks performed: HTML nesting and local links/anchors; 11 project entries; 23 certificate links; desktop and 390px mobile review; keyboard disclosure behavior; two PDF pages rendered and visually inspected.
