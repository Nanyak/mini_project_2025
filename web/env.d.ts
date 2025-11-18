/// <reference types="vite/client" />

declare module "*.vue" {
  import type { DefineComponent } from "vue"
  // biome-ignore lint/suspicious/noExplicitAny: Vue component type requires any
  // biome-ignore lint/complexity/noBannedTypes: Vue component type definition
  const component: DefineComponent<{}, {}, any>
  export default component
}
