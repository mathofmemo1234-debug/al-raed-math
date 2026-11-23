# -*- coding: utf-8 -*-
import re, sys

sys.stdout.reconfigure(encoding='utf-8')

def tokenize_ar_math(expr):
    frac_map = {}
    def save_frac(m):
        key = f"___FRAC_{len(frac_map)}___"
        frac_map[key] = m.group(0)
        return f" {key} "
    
    # Match outer span of ar-frac (contains two inner spans)
    clean_expr = re.sub(r'<span class="ar-frac">[\s\S]*?</span>\s*</span>', save_frac, expr)
    
    other_map = {}
    def save_tag(m):
        key = f"___TAG_{len(other_map)}___"
        other_map[key] = m.group(0)
        return f" {key} "
    
    clean_expr = re.sub(r'<[^>]+>', save_tag, clean_expr)
    
    parts = re.split(r'(\s+|[=×÷+−≤≥<>≠←→⟸]|(?<=\s)-(?=\s))', clean_expr)
    
    span_tokens = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        for k, v in frac_map.items():
            p = p.replace(k, v)
        for k, v in other_map.items():
            p = p.replace(k, v)
            
        if p.startswith('<span class="ar-frac">') and p.endswith('</span>'):
            span_tokens.append(p)
        else:
            span_tokens.append(f'<span>{p}</span>')
            
    return ' '.join(span_tokens)

samples = [
    '<span class="ar-frac"><span class="num">٢</span><span class="denom">٣</span></span> = <span class="ar-frac"><span class="num">٦</span><span class="denom">٩</span></span>',
    '٠,٢ × ٠,٣ = ٠,٦'
]

for s in samples:
    print('INPUT: ', s)
    print('OUTPUT:', tokenize_ar_math(s))
    print('-'*50)
