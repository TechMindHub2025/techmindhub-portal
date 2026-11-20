---
title: "GitHub Extends OIDC Audit Streaming to GHE.com: Short-Lived Credentials, New Trust Boundaries"
description: "GHE.com enterprises can stream audit logs to Amazon S3 using OIDC rather than stored AWS access keys. The destination and IAM trust policy still demand careful review."
excerpt: "The audit stream can use temporary AWS credentials, while its storage destination remains an explicit governance choice."
pubDate: "2026-11-20T06:14:00Z"
status: "published"
cover_card: "https://media.techmindhub.cc/posts/github-ghe-oidc-audit-s3-streaming-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/github-ghe-oidc-audit-s3-streaming-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/github-ghe-oidc-audit-s3-streaming-og-web-v1.jpg"
card_alt: "A temporary identity token carries audit records toward a guarded storage bucket."
cover_alt: "Conceptual GitHub audit stream through OIDC and AWS temporary credentials to an S3 bucket, with IAM and residency boundaries."
canonical_id: "2026-11-20-github-ghe-oidc-audit-s3-streaming"
tags: ["GitHub", "OIDC", "AuditLogs", "CloudSecurity", "TechMindHub"]
source_url: "https://github.blog/changelog/2026-11-19-s3-audit-log-streaming-with-openid-connect-expands-to-ghe-com/"
domain: "infrastructure"
topic: "Federated audit delivery"
---

An audit stream must run continuously, which has often meant leaving a long-lived cloud key in the system that exports the logs. [GitHub's November 19 update](https://github.blog/changelog/2026-11-19-s3-audit-log-streaming-with-openid-connect-expands-to-ghe-com/) extends its Amazon S3 audit-log streaming with OpenID Connect to **GitHub Enterprise Cloud with data residency**, hosted on GHE.com. The capability already existed for enterprises on github.com. Administrators can now avoid storing permanent AWS access keys in GitHub for this GHE.com route.

## A token replaces the stored key

The [configuration guide](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise) describes an AWS IAM OIDC provider, a role trust policy and an S3 write policy. GitHub presents an identity token, AWS Security Token Service validates it against the configured issuer and audience, and the role grants temporary credentials for delivery. This changes the secret's lifetime and custody; it does not make the write permission unimportant.

The trust policy must constrain the audience to `sts.amazonaws.com` and the subject to the precise enterprise identity. For GHE.com, GitHub documents a case-sensitive subject of the form `https://SUBDOMAIN.ghe.com`. If an enterprise changes its subdomain, retaining an old trusted subject can leave an obsolete identity path in the AWS role. The bucket policy, public-access block, encryption, retention and monitoring still need their own review.

## Data residency has a destination

GHE.com data residency does not automatically make an AWS bucket reside in the same region. GitHub explicitly warns that streaming exports audit records to the bucket and AWS region selected by the enterprise, potentially outside its residency region. The receiving account, region, retention rules and access to the resulting logs are therefore part of the deployment decision.

The practical test is end to end: create a least-privilege role, configure the stream, confirm new events arrive, check for gaps and alerts if delivery stops, then remove any old static credentials only after continuity is demonstrated. OIDC reduces one class of credential risk. It does not correct an overly broad IAM policy or make an unmonitored audit pipeline reliable.

## Sources

- [GitHub Changelog: S3 audit log streaming with OIDC expands to GHE.com, November 19, 2026](https://github.blog/changelog/2026-11-19-s3-audit-log-streaming-with-openid-connect-expands-to-ghe-com/)
- [GitHub Docs: Streaming the enterprise audit log](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise)
