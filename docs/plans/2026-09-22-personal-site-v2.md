# Personal website v2 implementation plan

Goal: create the approved light, spacious personal website as a separate v2, preserving v1.
Architecture: four static HTML pages sharing local CSS. Existing approved content is retained; project details use native accessible disclosures. A separate concise two-page PDF offers a downloadable CV.
Tech stack: HTML, CSS, Python content transformation, ReportLab PDF.

1. Extract approved experience, projects, skills, learning and reading from index.html without modifying it.
2. Build v2/index.html, experience.html, projects.html, learning.html and assets/style.css. Use semantic navigation, accessible project disclosures, responsive layouts and reduced-motion support.
3. Generate v2/assets/roberto-segura-cv.pdf from confirmed content. Render and inspect pages.
4. Check local links, preserved 23 certificate URLs, seven professional and four personal projects, and keyboard disclosures. Inspect desktop/mobile through browser and fix overflow or spacing issues.
5. Open v2 for comparison. Preserve the original index.html and do not publish externally.
