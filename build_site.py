NEXORA_BUSINESS/
├── index.html
├── robots.txt
└── build_site.py
import os

folder = "NEXORA_BUSINESS"
os.makedirs(folder, exist_ok=True)

html = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>NEXORA BUSINESS | Digital Solutions</title>
<meta name="description" content="NEXORA BUSINESS offers web development, graphic design, digital marketing and cyber security services.">

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    scroll-behavior: smooth;
}

body {
    background: #070b18;
    color: white;
    font-family: Arial, sans-serif;
}

nav {
    position: sticky;
    top: 0;
    z-index: 10;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 22px 8%;
    background: #10182c;
}

.logo {
    color: #00eaff;
    font-size: 26px;
    font-weight: bold;
}

nav a {
    color: white;
    text-decoration: none;
    margin-left: 20px;
}

nav a:hover {
    color: cyan;
}

.hero {
    min-height: 85vh;
    padding: 70px 8%;
    display: flex;
    align-items: center;
    justify-content: space-around;
    flex-wrap: wrap;
    background: radial-gradient(circle at 75% 50%,
                #123c66, #070b18 60%);
}

.hero-content {
    max-width: 550px;
}

.hero h1 {
    font-size: clamp(40px, 6vw, 65px);
    margin-bottom: 20px;
}

.hero h1 span {
    color: cyan;
}

.hero p {
    color: #bbc5d7;
    line-height: 1.8;
    margin-bottom: 25px;
}

.btn {
    display: inline-block;
    padding: 15px 30px;
    border: none;
    border-radius: 30px;
    background: cyan;
    color: #06101c;
    font-weight: bold;
    text-decoration: none;
    cursor: pointer;
}

.btn:hover {
    box-shadow: 0 0 25px cyan;
    transform: translateY(-4px);
}

.scene {
    width: 160px;
    height: 160px;
    perspective: 600px;
    margin: 70px;
}

.cube {
    position: relative;
    width: 100%;
    height: 100%;
    transform-style: preserve-3d;
    animation: rotate 7s linear infinite;
}

.face {
    position: absolute;
    width: 160px;
    height: 160px;
    border: 3px solid cyan;
    background: #00eaff22;
    box-shadow: 0 0 25px #00eaff66;
}

.front { transform: translateZ(80px); }
.back { transform: rotateY(180deg) translateZ(80px); }
.right { transform: rotateY(90deg) translateZ(80px); }
.left { transform: rotateY(-90deg) translateZ(80px); }
.top { transform: rotateX(90deg) translateZ(80px); }
.bottom { transform: rotateX(-90deg) translateZ(80px); }

@keyframes rotate {
    from { transform: rotateX(0) rotateY(0); }
    to { transform: rotateX(360deg) rotateY(360deg); }
}

section {
    padding: 75px 8%;
}

.heading {
    text-align: center;
    font-size: 38px;
    margin-bottom: 40px;
}

.heading span {
    color: cyan;
}

.services {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 25px;
}

.card {
    width: 260px;
    padding: 30px;
    background: #15213b;
    border: 1px solid #00eaff66;
    border-radius: 18px;
    transition: .3s;
}

.card:hover {
    transform: translateY(-10px);
    box-shadow: 0 0 25px #00eaff55;
}

.card h3 {
    color: cyan;
    margin-bottom: 15px;
}

.card p {
    color: #bbc5d7;
    line-height: 1.7;
}

.about {
    background: #10182c;
    text-align: center;
}

.about p {
    max-width: 750px;
    margin: auto;
    line-height: 1.9;
    color: #bbc5d7;
}

.contact {
    text-align: center;
}

form {
    max-width: 500px;
    margin: auto;
}

input, textarea {
    display: block;
    width: 100%;
    padding: 15px;
    margin: 12px 0;
    border: 1px solid cyan;
    border-radius: 10px;
    background: #111b30;
    color: white;
}

textarea {
    min-height: 120px;
}

footer {
    padding: 25px;
    background: #10182c;
    text-align: center;
    color: #bbc5d7;
}

@media(max-width: 650px) {
    nav {
        flex-direction: column;
        gap: 15px;
    }

    nav a {
        margin: 6px;
        font-size: 14px;
    }

    .hero {
        text-align: center;
    }

    .scene {
        margin: 70px auto;
    }
}
</style>
</head>

<body>

<nav>
    <div class="logo">NEXORA.</div>
    <div>
        <a href="#home">Home</a>
        <a href="#services">Services</a>
        <a href="#about">About</a>
        <a href="#contact">Contact</a>
    </div>
</nav>

<section class="hero" id="home">
    <div class="hero-content">
        <h1>Build Your <span>Digital Future</span></h1>
        <p>
            We help businesses grow with modern technology,
            creative web design and digital solutions.
        </p>
        <a href="#services" class="btn">Explore Services</a>
    </div>

    <div class="scene">
        <div class="cube">
            <div class="face front"></div>
            <div class="face back"></div>
            <div class="face right"></div>
            <div class="face left"></div>
            <div class="face top"></div>
            <div class="face bottom"></div>
        </div>
    </div>
</section>

<section id="services">
    <h2 class="heading">Our <span>Services</span></h2>
    <div class="services">
        <div class="card">
            <h3>Web Development</h3>
            <p>Responsive and modern business websites.</p>
        </div>
        <div class="card">
            <h3>Graphic Design</h3>
            <p>Creative branding and visual design.</p>
        </div>
        <div class="card">
            <h3>Cyber Security</h3>
            <p>Website security and digital safety services.</p>
        </div>
        <div class="card">
            <h3>Digital Marketing</h3>
            <p>Digital strategies for business growth.</p>
        </div>
    </div>
</section>

<section class="about" id="about">
    <h2 class="heading">About <span>NEXORA</span></h2>
    <p>
        NEXORA BUSINESS is a digital agency focused on
        modern web development, creative design and
        technology solutions. Our goal is to help
        businesses build a professional online presence.
    </p>
</section>

<section class="contact" id="contact">
    <h2 class="heading">Contact <span>Us</span></h2>

    <form action="https://formsubmit.co/YOUR_EMAIL@example.com"
          method="POST">

        <input type="hidden" name="_subject"
               value="New NEXORA Business Enquiry">

        <input type="text" name="name"
               placeholder="Your Name" required>

        <input type="email" name="email"
               placeholder="Your Email" required>

        <textarea name="message"
                  placeholder="Your Message"
                  required></textarea>

        <button type="submit" class="btn">
            Send Message
        </button>
    </form>
</section>

<footer>
    © 2026 NEXORA BUSINESS. All Rights Reserved.
</footer>

</body>
</html>
"""

robots = """User-agent: *
Allow: /
"""

with open(os.path.join(folder, "index.html"),
          "w", encoding="utf-8") as f:
    f.write(html)

with open(os.path.join(folder, "robots.txt"),
          "w", encoding="utf-8") as f:
    f.write(robots)

print("================================")
print(" NEXORA BUSINESS FILES CREATED!")
print("================================")
print("Folder:", os.path.abspath(folder))
print("Files: index.html, robots.txt")
print("Next: Open the index.html file in your browser.")
