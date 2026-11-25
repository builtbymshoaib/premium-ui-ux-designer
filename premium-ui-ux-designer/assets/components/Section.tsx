import type { ReactNode } from "react";
export function Section({ id, title, children }: { id: string; title: string; children: ReactNode }) {
  return <section id={id} aria-labelledby={`${id}-title`} className="ui-section"><div className="ui-container"><h2 id={`${id}-title`}>{title}</h2>{children}</div></section>;
}
