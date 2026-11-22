---
title: "Beyond HTTP: Cloudflare Opens a Bidirectional TCP Path to Edge Containers"
description: "Inbound TCP for Workers and bidirectional gRPC in Containers enter public beta, expanding edge application designs while introducing long-lived connection trade-offs."
excerpt: "A Worker can forward a byte stream through a Durable Object to a container that terminates TLS and runs gRPC."
pubDate: "2026-11-22T06:19:00Z"
status: "published"
cover_card: "https://media.techmindhub.cc/posts/cloudflare-inbound-tcp-grpc-edge-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/cloudflare-inbound-tcp-grpc-edge-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/cloudflare-inbound-tcp-grpc-edge-og-web-v1.jpg"
card_alt: "Two-way data stream passes through an edge node toward a container."
cover_alt: "Conceptual bidirectional path from TCP client through Spectrum, Worker and Durable Object to a gRPC server in a container."
canonical_id: "2026-11-22-cloudflare-inbound-tcp-grpc-edge"
tags: ["Infrastructure", "EdgeComputing", "TCP", "gRPC", "Cloudflare", "TechMindHub"]
source_url: "https://developers.cloudflare.com/changelog/post/2026-11-19-inbound-tcp/"
domain: "infrastructure"
topic: "Bidirectional edge services"
---

HTTP request handlers are a natural fit for many edge applications. A voice stream or a long-lived native protocol needs a different connection model. On November 19, [Cloudflare introduced public-beta inbound TCP for Workers and bidirectional gRPC in Containers](https://developers.cloudflare.com/changelog/post/2026-11-19-inbound-tcp/). Its example routes a public TCP connection through Spectrum to a Worker's `connect()` handler, then through a Durable Object to a container running a gRPC server.

The Worker and Durable Object forward bytes in both directions. In Cloudflare's documented example, **the container terminates TLS** and handles HTTP/2 and gRPC; the intermediary code is not claiming to interpret every message. The example enables TCP half-closes to preserve a normal streaming behavior. This can support services such as real-time voice interactions where the client and server exchange data continuously.

## A longer-lived edge contract

Passing a stream through several components changes the engineering questions. A service has to handle backpressure so a fast sender does not overwhelm a slow consumer, close both directions cleanly, recover from disconnects and account for container startup and readiness. Operators should test how connection duration, routing and state management behave under load and failure. The availability of a TCP path does not by itself prove the application will meet a particular latency or reliability target.

Cloudflare's documented reference also defines a practical boundary for early adoption. Worker-origin Spectrum applications are available on Pro and Business zones and on Enterprise zones with Spectrum Enterprise enabled. Without Spectrum Enterprise, Pro and Business zones support **one Worker-origin application per zone on one TCP port**. The feature is in public beta, so production suitability and service terms should be checked against the actual deployment.

The larger architectural change is that the edge Worker can act as a programmable stream entry point while the container hosts an existing protocol server. Whether that simplifies a system depends on how the team handles TLS, connection lifecycle, state and the failure of each intermediary.

## Source

- [Cloudflare: Inbound TCP and gRPC for Workers and Containers, November 19, 2026](https://developers.cloudflare.com/changelog/post/2026-11-19-inbound-tcp/)
