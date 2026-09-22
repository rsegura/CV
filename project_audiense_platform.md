---
name: audiense-platform-overview
description: "Audiense data platform architecture — Soyuz updaters, Trino Hubble/Cosmos, Vega API, Stasi entity resolution, Iceberg data lake"
metadata:
  type: project
---

Audiense data platform spans several interconnected systems in ~/Develop:

**Soyuz data lake** (9 updater repos): each service enriches one demographic dimension of Twitter profiles into Iceberg/Parquet tables. Active migration: followings_v2 to Iceberg format.

**Trino cluster "insights"**: two main query sources — Hubble (segmentation, ~73% executions, 86% CPU) and Cosmos (reporting pipeline). Known issues: dynamic filter collapse at 50k values, S3 read bottleneck at 15 concurrent readers, twitter_users JOINs consuming 91.8 TB/month network.

**Vega API** (6 repos): FastAPI with async job pattern, Athena/Trino routing, Redis rate limiting. Has admin panel, interest inferrer, Redpanda connectors, Iceberg reinference connector.

**Stasi**: entity canonical map builder — weekly CronJob resolving TikTok NER mentions to Wikidata identities, publishing immutable Iceberg snapshots.

**Why:** Understanding these connections is essential for any work in ~/Develop — most repos are interdependent through the Iceberg data lake.

**How to apply:** When working in any Soyuz, Vega, or Stasi repo, consider the downstream effects on the other systems. Trino query changes affect both Hubble and Cosmos.
