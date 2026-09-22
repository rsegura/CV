---
name: blog-embeddings-classifier
description: "Blog post 'Two models, one AND' — taxonomy classifier for TikTok interests using bi-encoder + cross-encoder intersection. 4 versions (EN/ES × v1/v2), ~20 diagrams, active as of 2026-09-18."
metadata:
  type: project
---

Blog post for the Audiense engineering blog: **"Two models, one AND: how agreement beat confidence in our taxonomy classifier"**. Lives in `~/Develop/blog_embeddings/`.

Content: documents the production pipeline that classifies TikTok entity text into a fixed taxonomy of ~444 interest categories.

Architecture:
1. **LoRA fine-tune** of a bi-encoder (308M params, 1.6% trainable via LoRA). MNRL loss + 5 hard negatives per positive + Matryoshka loss (128/256/512/768 dims). F1: 0.255 → 0.390 (+53%). Training: 22 min on M4 Max.
2. **Recall + rerank**: bi-encoder top-20 candidates (~3ms) → cross-encoder scores all 20 (~400ms).
3. **Intersection rule**: `final = [c for c in embedding_top5 if c in rerank_top5]`. No threshold on reranker score. Strict precision 36% → 52%.

Key finding: model agreement (both models ranking a category in top-5) is a stronger signal than any single model's confidence score. A category at reranker 0.95 not in bi-encoder top-5 had ~38% precision; one at 0.05 in bi-encoder top-5 had ~68%.

Files: 4 markdown versions (EN/ES × v1/v2), ~20 PNG diagrams, 1 generated PDF. Modified 2026-09-18 — active work.

**Why:** This is Roberto's first engineering blog post and represents deep applied ML knowledge. The insights (attractor categories, intersection > threshold, save-then-reload as unit test) are reusable across future classification work.

**How to apply:** When working on classification, embedding, or IR tasks, reference this architecture. The labeling pipeline ($0.30 with LLM-as-judge) and the LoRA recipe are directly reusable patterns.
