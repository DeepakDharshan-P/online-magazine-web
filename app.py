from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Structured data organizing magazines by topic with creator names
    magazine_catalog = [
        {
            "topic_name": "Technology & AI",
            "topic_slug": "tech",
            "magazines": [
                {
                    "title": "The Neural Network",
                    "creator": "Elena Rostova",
                    "issue": "Issue #42",
                    "excerpt": "Exploring the shift toward decentralized, sovereign AI architectures.",
                    "image": "https://picsum.photos/400/500?random=11"
                },
                {
                    "title": "Silicon Bound",
                    "creator": "Marcus Vance",
                    "issue": "Summer 2026",
                    "excerpt": "Are next-gen solid-state batteries finally ready for prime time?",
                    "image": "https://picsum.photos/400/500?random=12"
                },
                {
                    "title": "Ctrl+Alt+Shift",
                    "creator": "Sarah Jenkins",
                    "issue": "Vol. 8",
                    "excerpt": "The digital nomads leaving tech hubs for countryside communes.",
                    "image": "https://picsum.photos/400/500?random=13"
                }
            ]
        },
        {
            "topic_name": "Art & Design",
            "topic_slug": "design",
            "magazines": [
                {
                    "title": "Brutalist Spaces",
                    "creator": "Hiroshi Tanaka",
                    "issue": "Ed. 19",
                    "excerpt": "Reimagining raw concrete architecture in modern metropolitan landscapes.",
                    "image": "https://picsum.photos/400/500?random=21"
                },
                {
                    "title": "Chroma Theory",
                    "creator": "Amara Okafor",
                    "issue": "Issue #05",
                    "excerpt": "Why high-contrast neon palettes are dominating interactive application design.",
                    "image": "https://picsum.photos/400/500?random=22"
                },
                {
                    "title": "The Typographic",
                    "creator": "Linus Sterling",
                    "issue": "Special Issue",
                    "excerpt": "A study of variable font styling and its impact on reading comprehension.",
                    "image": "https://picsum.photos/400/500?random=23"
                }
            ]
        },
        {
            "topic_name": "Science & Space",
            "topic_slug": "science",
            "magazines": [
                {
                    "title": "Quantum Horizon",
                    "creator": "Dr. Aris Thorne",
                    "issue": "Vol. 14",
                    "excerpt": "Breaking down the recent breakthroughs in room-temperature quantum computing.",
                    "image": "https://picsum.photos/400/500?random=31"
                },
                {
                    "title": "Exosphere",
                    "creator": "Chloe Mercer",
                    "issue": "Issue #88",
                    "excerpt": "Deep space telemetry updates: What the Jupiter probes found this month.",
                    "image": "https://picsum.photos/400/500?random=32"
                },
                {
                    "title": "BioSynthesis",
                    "creator": "Dr. Neil Patel",
                    "issue": "Autumn Coll.",
                    "excerpt": "How synthetic biology is successfully engineering clean biofuel alternatives.",
                    "image": "https://picsum.photos/400/500?random=33"
                }
            ]
        }
    ]
    
    return render_template('index.html', catalog=magazine_catalog)

if __name__ == '__main__':
    app.run(debug=True)