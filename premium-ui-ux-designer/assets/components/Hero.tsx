import Link from "next/link";
export function Hero({ title, description, href, action }: { title: string; description: string; href: string; action: string }) {
  return <section className="ui-section"><div className="ui-container"><h1 className="ui-heading">{title}</h1><p style={{maxWidth:"65ch"}}>{description}</p><Link href={href} className="ui-button">{action}</Link></div></section>;
}
