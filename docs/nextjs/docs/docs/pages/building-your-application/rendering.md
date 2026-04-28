# Rendering
@last-updated: 2026-02-11


By default, Next.js **pre-renders** every page. This means that Next.js generates HTML for each page in advance, instead of having it all done by client-side JavaScript. Pre-rendering can result in better performance and SEO.

Each generated HTML is associated with minimal JavaScript code necessary for that page. When a page is loaded by the browser, its JavaScript code runs and makes the page fully interactive (this process is called [hydration](https://react.dev/reference/react-dom/client/hydrateRoot) in React).

### Pre-rendering

Next.js has two forms of pre-rendering: **Static Generation** and **Server-side Rendering**. The difference is in **when** it generates the HTML for a page.

* Static Generation: The HTML is generated at **build time** and will be reused on each request.
* Server-side Rendering: The HTML is generated on **each request**.

Importantly, Next.js lets you choose which pre-rendering form you'd like to use for each page. You can create a "hybrid" Next.js app by using Static Generation for most pages and using Server-side Rendering for others.

We recommend using Static Generation over Server-side Rendering for performance reasons. Statically generated pages can be cached by CDN with no extra configuration to boost performance. However, in some cases, Server-side Rendering might be the only option.

You can also use client-side data fetching along with Static Generation or Server-side Rendering. That means some parts of a page can be rendered entirely by clientside JavaScript. To learn more, take a look at the [Data Fetching](/docs/pages/building-your-application/data-fetching/client-side) documentation.

- [Server-side Rendering (SSR)](/docs/pages/building-your-application/rendering/server-side-rendering)
  - Use Server-side Rendering to render pages on each request.
- [Static Site Generation (SSG)](/docs/pages/building-your-application/rendering/static-site-generation)
  - Use Static Site Generation (SSG) to pre-render pages at build time.
- [Automatic Static Optimization](/docs/pages/building-your-application/rendering/automatic-static-optimization)
  - Next.js automatically optimizes your app to be static HTML whenever possible. Learn how it works here.
- [Client-side Rendering (CSR)](/docs/pages/building-your-application/rendering/client-side-rendering)
  - Learn how to implement client-side rendering in the Pages Router.

---

For an overview of all available documentation, see [/docs/llms.txt](/docs/llms.txt)