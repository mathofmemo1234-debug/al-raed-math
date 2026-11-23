import json, sys

sys.stdout.reconfigure(encoding='utf-8')

path = r"C:\Users\TOSHIBA\.gemini\antigravity\brain\9274f205-cb1c-4bb9-8c86-1ec6c89a08a9\.system_generated\logs\transcript.jsonl"
with open(path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line: continue
        try: obj = json.loads(line)
        except: continue
        for tc in obj.get("tool_calls", []):
            args = tc.get("args") or tc.get("arguments") or {}
            p = args.get("Path", "")
            if "render_final_pdfs.py" in p:
                print("Content of render_final_pdfs.py:")
                print(args.get("Content", ""))
