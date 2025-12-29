The Research Radar

A high-fidelity, responsive web interface for an AI Research Newsletter subscription service. Designed with a "cyber-grid" aesthetic, featuring a starfield background, glassmorphism UI, and interactive multi-step forms.

🚀 Features

Fully Responsive: Optimized for Mobile, Tablet, and Desktop (PC) with fluid typography and adaptive spacing.

Interactive Background: A dynamic 3D starfield canvas that reacts to system state, accelerating smoothly during the "sweep" phase.

Scanner Effect: A visual "radar scan" line that pulses and speeds up during the subscription sequence, transitioning smoothly back to a resting state.

Multi-Step Flow: A seamless 3-step transition (Targeting, Calibration, Protocol) using CSS transforms and state-aware navigation dots.

Glassmorphism UI: Modern frosted-glass effect with backdrop filters and subtle borders for a premium feel.

Tailwind CSS: Utilizes a utility-first approach for rapid styling and highly maintainable responsive layouts.

🛠️ Tech Stack

HTML5/CSS3 (Custom Animations & Canvas API)

JavaScript (Vanilla ES6+)

Tailwind CSS (via CDN)

Google Fonts (Inter & Roboto Mono)

📂 Project Structure

index.html: The main entry point containing all HTML structure, CSS styles (Tailwind), and the core JavaScript logic for the canvas engine and form state.

README.md: Project documentation and setup guide.

📥 How to Run Locally

Download the files: Ensure index.html is saved in your desired directory.

Open with Browser:

Double-click index.html.

OR right-click the file and select "Open with..." and choose your preferred browser (Chrome, Firefox, Safari, Edge).

No Server Required: Since this is a static frontend project using a CDN for Tailwind, you do not need to run a local server (like Node.js or Python) to view the interface.

🎨 Customization

Changing the Name

To change the branding from "Research Radar" to something else (e.g., "SOTA Sentinel"), search for the "< h1 >" tag in index.html and update the text.

Adjusting the Colors

The theme uses Tailwind's cyan-400 as the primary accent. You can replace cyan with emerald, indigo, or rose using a global find-and-replace to change the entire color scheme.

Modifying Interests

The "Calibration" step (Step 2) contains checkboxes for research interests. You can add or remove <label> blocks in the interest-list div to customize the topics offered to your subscribers.

📜 License

This project is open-source. Feel free to modify and use it for your own research newsletters or personal projects.