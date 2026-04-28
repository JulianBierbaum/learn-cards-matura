# typedRoutes
@doc-version: 16.1.6
@last-updated: 2026-02-11


> **Note**: This option has been marked as stable, so you should use `typedRoutes` instead of `experimental.typedRoutes`.

Support for [statically typed links](/docs/app/api-reference/config/typescript#statically-typed-links). This feature requires using TypeScript in your project.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  typedRoutes: true,
}

module.exports = nextConfig
```
---

For an overview of all available documentation, see [/docs/llms.txt](/docs/llms.txt)