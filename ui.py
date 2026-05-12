# ui.py

# Custom CSS for premium sci-fi UI/UX
custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700&family=Fira+Code:wght@400;500&display=swap');

/* Global styles with sci-fi gradient background */
body, .gradio-container {
    background: linear-gradient(135deg, #0a0a1a 0%, #1a1a3e 50%, #0a0a1a 100%) !important;
    color: #e0e0e0 !important;
    font-family: 'Fira Code', 'Courier New', monospace !important;
    min-height: 100vh !important;
}

.contain {
    background: transparent !important;
}

/* Main container - glassmorphism effect */
.main {
    background: rgba(10, 10, 26, 0.85) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(0, 212, 255, 0.15) !important;
    border-radius: 12px !important;
    margin: 20px !important;
    padding: 25px !important;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.8), 0 0 60px rgba(0, 212, 255, 0.05) !important;
}

/* Story text styling with improved readability */
.prose {
    color: #e0e0e0 !important;
    font-family: 'Fira Code', monospace !important;
    line-height: 1.9 !important;
    font-size: 15px !important;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5) !important;
}

.prose em {
    color: #00d4ff !important;
    font-style: italic !important;
}

.prose strong {
    color: #00ff88 !important;
    font-weight: 600 !important;
    text-shadow: 0 0 10px rgba(0, 255, 136, 0.3) !important;
}

/* Premium button styling with sci-fi gradients */
button.primary, button.lg {
    background: linear-gradient(145deg, #1a1a2e 0%, #2a2a4e 100%) !important;
    border: 1px solid #3a3a6e !important;
    border-radius: 8px !important;
    color: #e0e0e0 !important;
    font-family: 'Orbitron', sans-serif !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    padding: 14px 28px !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(0, 212, 255, 0.05) !important;
    position: relative !important;
    overflow: hidden !important;
}

button.primary:hover, button.lg:hover {
    background: linear-gradient(145deg, #2a2a4e 0%, #3a3a6e 100%) !important;
    border-color: #00d4ff !important;
    color: #00d4ff !important;
    box-shadow: 0 6px 25px rgba(0, 212, 255, 0.3), inset 0 1px 0 rgba(0, 212, 255, 0.1) !important;
    transform: translateY(-2px) !important;
}

button.primary:active, button.lg:active {
    transform: translateY(0) !important;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.4) !important;
}

button.secondary {
    background: linear-gradient(145deg, #1a1a1a 0%, #252525 100%) !important;
    border: 1px solid #333 !important;
    border-radius: 8px !important;
    color: #888 !important;
    font-family: 'Orbitron', sans-serif !important;
    font-size: 12px !important;
    font-weight: 400 !important;
    padding: 10px 20px !important;
    transition: all 0.3s ease !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
}

button.secondary:hover {
    background: linear-gradient(145deg, #252525 0%, #333 100%) !important;
    border-color: #00d4ff !important;
    color: #00d4ff !important;
}

/* Image container with premium border */
.image-container {
    border-radius: 10px !important;
    overflow: hidden !important;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.6), 0 0 40px rgba(0, 212, 255, 0.1) !important;
    border: 1px solid rgba(0, 212, 255, 0.2) !important;
}

.image-container img {
    border-radius: 10px !important;
    display: block !important;
}

/* Headers with sci-fi styling */
h1 {
    color: #00d4ff !important;
    font-family: 'Orbitron', sans-serif !important;
    text-transform: uppercase !important;
    letter-spacing: 4px !important;
    font-size: 28px !important;
    text-shadow: 0 0 20px rgba(0, 212, 255, 0.4), 0 2px 4px rgba(0, 0, 0, 0.8) !important;
    margin-bottom: 5px !important;
}

h2, h3 {
    color: #00ff88 !important;
    font-family: 'Orbitron', sans-serif !important;
    text-transform: uppercase !important;
    letter-spacing: 2px !important;
    text-shadow: 0 0 15px rgba(0, 255, 136, 0.3) !important;
}

/* Status panel glassmorphism */
.status-panel {
    background: rgba(20, 20, 40, 0.7) !important;
    backdrop-filter: blur(8px) !important;
    border: 1px solid rgba(0, 212, 255, 0.2) !important;
    border-radius: 10px !important;
    padding: 15px !important;
    box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.3) !important;
}

/* Divider styling */
hr {
    border: none !important;
    height: 1px !important;
    background: linear-gradient(90deg, transparent, rgba(0, 212, 255, 0.3), transparent) !important;
    margin: 20px 0 !important;
}

/* Scrollbar styling */
::-webkit-scrollbar {
    width: 8px !important;
}

::-webkit-scrollbar-track {
    background: #0a0a1a !important;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #3a3a6e, #2a2a4e) !important;
    border-radius: 4px !important;
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(180deg, #4a4a7e, #3a3a6e) !important;
}

/* Animation for text fade-in */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.fade-in {
    animation: fadeIn 0.5s ease-out !important;
}

/* Subtle pulse animation for important elements */
@keyframes pulse-glow {
    0%, 100% { box-shadow: 0 0 20px rgba(0, 212, 255, 0.2); }
    50% { box-shadow: 0 0 30px rgba(0, 212, 255, 0.4); }
}

.pulse {
    animation: pulse-glow 3s ease-in-out infinite !important;
}
"""

def build_status_panel(game_state):
    """Generate HTML for the status panel"""
    health = game_state["Player_Health"]
    
    # Calculate health bar color based on health level
    if health > 70:
        health_color = "#00ff88"
    elif health > 40:
        health_color = "#ffaa00"
    else:
        health_color = "#ff4444"
    
    # Calculate health bar width percentage
    health_percent = max(0, min(100, health))
    
    # Build inventory display
    inventory_items = []
    if game_state["Has_Scanner"]:
        inventory_items.append("Scanner")
    if game_state["Has_Artifact"]:
        inventory_items.append("Artifact Core")
    
    inventory_display = ", ".join(inventory_items) if inventory_items else "Empty"
    
    html = f"""
    <div class='status-panel'>
        <div style='margin-bottom: 15px;'>
            <span style='color: #00d4ff; font-family: "Orbitron", sans-serif; font-weight: 600; font-size: 13px; text-transform: uppercase; letter-spacing: 2px;'>⚡ HEALTH</span>
            <div style='margin-top: 8px; background: rgba(0, 0, 0, 0.5); border: 1px solid rgba(0, 212, 255, 0.3); border-radius: 4px; height: 20px; overflow: hidden;'>
                <div style='background: linear-gradient(90deg, {health_color}, {health_color}88); height: 100%; width: {health_percent}%; transition: width 0.3s ease;'></div>
            </div>
            <div style='color: #e0e0e0; margin-top: 4px; font-size: 12px; text-align: right;'>{health} / 100</div>
        </div>
        <div style='margin-top: 15px; padding-top: 12px; border-top: 1px solid rgba(0, 212, 255, 0.2);'>
            <span style='color: #00d4ff; font-family: "Orbitron", sans-serif; font-weight: 600; font-size: 13px; text-transform: uppercase; letter-spacing: 2px;'>📡 INVENTORY</span>
            <div style='color: #e0e0e0; margin-top: 6px; font-size: 13px;'>{inventory_display}</div>
        </div>
    </div>
    """
    return html
