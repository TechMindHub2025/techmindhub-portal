---
title: "SOPS: Version the Configuration, Control Access to Its Secrets"
description: "SOPS keeps structured configuration in version control while encrypting values. A useful workflow must also manage editing environments, recipients, data keys and the underlying credentials."
excerpt: "Encrypted configuration can travel with application changes, but reviewing its structure is different from verifying a hidden value or rotating a credential."
pubDate: "2026-10-30"
status: "published"
canonical_id: "2026-10-30-sops-versioned-encrypted-configuration"
tags: ["OpenSource", "SecretsManagement", "GitOps", "DevSecOps", "DeveloperTools", "TechMindHub"]
source_url: "https://github.com/getsops/sops/releases/tag/v3.13.3"
cover_card: "https://media.techmindhub.cc/posts/sops-versioned-encrypted-configuration-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/sops-versioned-encrypted-configuration-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/sops-versioned-encrypted-configuration-og-web-v1.jpg"
domain: "digital-trust"
topic: "Encrypted configuration"
card_alt: "Conceptual structured configuration with opaque encrypted values and an access boundary under the words Version the Structure."
cover_alt: "Conceptual diagram showing visible field names, encrypted values, authorised editing and separate file-key and service-credential changes."
---

Application configuration often changes with the application itself. Version control can preserve that relationship, but a plain-text configuration file is the wrong place to put passwords or API tokens. [SOPS](https://github.com/getsops/sops) provides a way to edit and version encrypted configuration files in formats including YAML, JSON, ENV and INI.

As of October 30, 2026, the project's release page lists [v3.13.3](https://github.com/getsops/sops/releases/tag/v3.13.3), released July 23, as the latest version. This is an established open-source tool under maintenance, rather than a newly announced product. SOPS can use local age identities or supported key-management services.

For structured files, the default behaviour leaves field names readable while encrypting values. A reviewer can see a file's shape and encrypted history without seeing the secret values. Field names themselves may still reveal sensitive architecture, so they need review too. The visibility of structure also has a limit: a changed ciphertext cannot tell a reviewer whether the hidden password is correct.

With recipients configured and an authorised decryption identity available, an operator can edit an existing encrypted YAML file:

```sh
sops edit secrets.yaml
```

SOPS decrypts the file for the editor and re-encrypts it when editing ends. The editor, its temporary files, shell history, local storage and deployment environment are therefore part of the trust boundary. Encrypting the committed file does not automatically make those places safe.

## Test the full deployment path

Our engineering assessment is to begin with dummy credentials and a bounded service configuration. Add a second database connection, for example, and check whether reviewers can identify the new field without seeing its value. Have an authorised operator edit and recover the file, then confirm a separate environment without the necessary identity cannot decrypt it.

Next, follow plaintext into deployment. Identify where decryption happens, who can access the result, whether logs or intermediate files retain it and how a failed deployment is recovered. A change can be reviewable in Git while the actual secret still leaks at runtime if this handoff is careless.

## Separate keys from credentials

[SOPS key-management documentation](https://getsops.io/docs/usage/key-management/) distinguishes updating recipients with `updatekeys` from rotating the file's data-encryption key with `rotate`. It also treats replacement of passwords and API tokens *inside* the document as another operation. Re-encrypting a file does not invalidate a database password. Removing a recipient cannot retract plaintext that person already obtained or erase an accessible historical copy.

An operating procedure should state who adds and removes recipients, who rotates file keys, and who changes service credentials when access is compromised or a person leaves. Keep a recovery identity and test it. The sequence should be designed around the actual threat and the copy history, not inferred from the presence of encryption in a repository.

SOPS makes it practical to version configuration beside code while controlling access to secret values. Its value depends on maintaining the complete editing, deployment and credential-rotation process around the file.

## Sources

- [SOPS project](https://github.com/getsops/sops)
- [Release v3.13.3](https://github.com/getsops/sops/releases/tag/v3.13.3)
- [Usage and key management](https://getsops.io/docs/usage/key-management/)
