"use client";
import { useId, useRef, useState } from "react";
import Link from "next/link";
export function Navigation({ links, currentPath }: { links: { href: string; label: string }[]; currentPath: string }) {
  const [open, setOpen] = useState(false);
  const id = useId(); const trigger = useRef<HTMLButtonElement>(null);
  return <nav className="ui-nav" aria-label="Primary" onKeyDown={e => { if (e.key === "Escape" && open) { setOpen(false); trigger.current?.focus(); } }}>
    <button type="button" ref={trigger} aria-expanded={open} aria-controls={id} onClick={() => setOpen(v => !v)}>Menu</button>
    <div id={id} hidden={!open}><ul>{links.map(link => <li key={link.href}><Link href={link.href} aria-current={currentPath === link.href ? "page" : undefined} onClick={() => { setOpen(false); trigger.current?.focus(); }}>{link.label}</Link></li>)}</ul></div>
  </nav>;
}
