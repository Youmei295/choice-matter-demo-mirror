# scenes.py

# Complete 21-scene database for The Kepler Artifact
SCENES = {
    "001": {
        "text": "Your ship lands violently on the rocky surface of Kepler-186f. Purple fog crawls across the ground beneath a storm-filled sky. A metallic object pulses with blue light nearby while a dark cave entrance disappears into the cliffs beyond.",
        "image": "assets/kepler_landing.png",
        "choices": [
            ("Touch the artifact", "002", "damage_20"),
            ("Scan the artifact", "003", "check_scanner"),
            ("Ignore it and head toward the cave", "004", None)
        ],
        "isTerminal": False
    },
    "002": {
        "text": "The moment your hand touches the metal surface, a surge of energy tears through your body. Your vision fractures into flashes of alien cities and collapsing stars. A map suddenly appears on your visor HUD, pointing toward a hidden underground structure.",
        "image": "assets/kepler_artifact.png",
        "choices": [
            ("Follow the underground map", "005", None),
            ("Return to the ship", "006", None)
        ],
        "isTerminal": False
    },
    "003": {
        "text": "Your scanner emits rapid warning tones. The object contains an immense but unstable power source. Beneath the surface, faint signals pulse in response to the artifact. You carefully extract a glowing energy core from the device.",
        "image": "assets/kepler_scan.png",
        "choices": [
            ("Store the artifact safely", "007", "add_artifact"),
            ("Track the underground signal", "005", None)
        ],
        "isTerminal": False
    },
    "004": {
        "text": "The cave walls glow faintly with alien symbols that pulse like veins beneath stone. Deeper inside, a massive biomechanical creature coils around a pedestal, motionless beneath layers of dust.",
        "image": "assets/kepler_cave.png",
        "choices": [
            ("Sneak past the creature", "008", None),
            ("Attempt communication", "009", None),
            ("Retreat quietly", "006", None)
        ],
        "isTerminal": False
    },
    "005": {
        "text": "An enormous underground complex stretches beneath the planet's crust. Rows of shattered cryogenic chambers line the walls while dormant reactors hum faintly in the darkness. As you step forward, the facility begins to awaken.",
        "image": "assets/kepler_cave.png",
        "choices": [
            ("Shut down the reactor", "010", None),
            ("Restore full power", "011", None)
        ],
        "isTerminal": False
    },
    "006": {
        "text": "You decide the mission has become too dangerous. But as your ship prepares for launch, every monitor flickers with strange symbols. Something from the planet has entered your systems.",
        "image": "assets/kepler_ship.png",
        "choices": [
            ("Purge the ship systems", "012", None),
            ("Ignore the warnings", "013", None)
        ],
        "isTerminal": False
    },
    "007": {
        "text": "The artifact is locked safely inside a reinforced containment unit. Yet even through the shielding, the blue glow grows stronger with every passing minute.",
        "image": "assets/kepler_scan.png",
        "choices": [
            ("Open the containment unit", "014", None),
            ("Destroy the artifact", "015", None)
        ],
        "isTerminal": False
    },
    "008": {
        "text": "As you move past the creature, a loose stone cracks beneath your boot. Red eyes snap open in the darkness. Before you can react, a beam of light vaporizes you instantly.\n\n[GAME OVER — THE TRESPASSER]",
        "image": "assets/kepler_death.png",
        "choices": [
            ("Restart", "001", "reset")
        ],
        "isTerminal": True
    },
    "009": {
        "text": "The creature slowly raises its head as your translator emits greeting signals. To your surprise, it responds calmly. It explains that its civilization destroyed itself through war and greed. 'Will humanity repeat our failure?' it asks.",
        "image": "assets/kepler_diplomat.png",
        "choices": [
            ("Promise peace", "016", None),
            ("Demand alien technology", "017", None)
        ],
        "isTerminal": False
    },
    "010": {
        "text": "You shut down the ancient reactor permanently. The underground city fades back into darkness. Humanity will never know what was hidden beneath Kepler-186f.\n\n[ENDING — THE SILENCE]",
        "image": "assets/kepler_death.png",
        "choices": [
            ("Restart", "001", "reset")
        ],
        "isTerminal": True
    },
    "011": {
        "text": "Power floods through the underground city. Towers of blue light ignite across the darkness while massive machines awaken beneath the floor. Warning alarms echo through the facility as defense systems activate.",
        "image": "assets/kepler_cave.png",
        "choices": [
            ("Escape immediately", "018", None),
            ("Stay and investigate", "019", None)
        ],
        "isTerminal": False
    },
    "012": {
        "text": "You destroy the infected ship systems before the signal can spread further. The journey home is nearly fatal, but you survive. Humanity never learns the truth about Kepler-186f.\n\n[ENDING — THE SURVIVOR]",
        "image": "assets/kepler_victory.png",
        "choices": [
            ("Restart", "001", "reset")
        ],
        "isTerminal": True
    },
    "013": {
        "text": "The strange signal spreads silently through your ship systems during the return journey. By the time you reach Earth, it has already infiltrated global networks. Humanity never notices the invasion beginning.\n\n[ENDING — THE SIGNAL]",
        "image": "assets/kepler_death.png",
        "choices": [
            ("Restart", "001", "reset")
        ],
        "isTerminal": True
    },
    "014": {
        "text": "The containment unit opens and blue light floods the room. Suddenly you experience the memories of an alien civilization: towering cities, peaceful oceans, and finally total destruction through endless war.",
        "image": "assets/kepler_artifact.png",
        "choices": [
            ("Share the knowledge with Earth", "020", None),
            ("Keep the truth secret", "021", None)
        ],
        "isTerminal": False
    },
    "015": {
        "text": "You attempt to destroy the artifact. The core destabilizes instantly and erupts in a violent explosion that consumes the entire chamber.\n\n[ENDING — THE FOOL]",
        "image": "assets/kepler_death.png",
        "choices": [
            ("Restart", "001", "reset")
        ],
        "isTerminal": True
    },
    "016": {
        "text": "The guardian studies you silently before granting humanity advanced medicine and clean energy technology. Humanity is judged worthy of inheriting the knowledge of a fallen civilization.\n\n[TRUE ENDING — THE DIPLOMAT]",
        "image": "assets/kepler_diplomat.png",
        "choices": [
            ("Restart", "001", "reset")
        ],
        "isTerminal": True
    },
    "017": {
        "text": "The guardian's eyes burn red as it realizes humanity seeks power rather than understanding. Ancient defense systems awaken beneath the planet and erase your expedition completely.\n\n[ENDING — THE CONQUEROR]",
        "image": "assets/kepler_death.png",
        "choices": [
            ("Restart", "001", "reset")
        ],
        "isTerminal": True
    },
    "018": {
        "text": "You flee the collapsing underground city just before the ancient systems overload. Earth celebrates you as a hero, but you can never forget what still sleeps beneath Kepler-186f.\n\n[ENDING — THE ESCAPEE]",
        "image": "assets/kepler_ship.png",
        "choices": [
            ("Restart", "001", "reset")
        ],
        "isTerminal": True
    },
    "019": {
        "text": "You remain inside the awakened city and discover preserved alien consciousnesses stored within an immense archive. Choosing knowledge over mortality, you upload your own mind into the system forever.\n\n[SECRET ENDING — THE ARCHIVIST]",
        "image": "assets/kepler_victory.png",
        "choices": [
            ("Restart", "001", "reset")
        ],
        "isTerminal": True
    },
    "020": {
        "text": "Humanity unites around the knowledge recovered from Kepler-186f. Disease, famine, and energy shortages disappear within decades as civilization enters a new golden age.\n\n[ENDING — THE RENAISSANCE]",
        "image": "assets/kepler_victory.png",
        "choices": [
            ("Restart", "001", "reset")
        ],
        "isTerminal": True
    },
    "021": {
        "text": "You hide the truth about the artifact from the world. Governments and corporations hunt you endlessly while the blue glow of the artifact continues pulsing in the darkness beside you.\n\n[ENDING — THE KEEPER]",
        "image": "assets/kepler_artifact.png",
        "choices": [
            ("Restart", "001", "reset")
        ],
        "isTerminal": True
    }
}
