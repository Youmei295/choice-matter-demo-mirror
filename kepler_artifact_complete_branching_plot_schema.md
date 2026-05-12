# The Kepler Artifact — Complete Simple Choice Game Plot

## Purpose
This document defines the complete story structure for a simple click-and-choice narrative game.

The structure is intentionally designed so:
- a human developer can implement it easily
- an AI model can later read and expand it
- scenes are modular
- branching remains manageable

No AI-driven generation is assumed yet.

---

# WORLD SETTING

## Planet
Kepler-186f

## Tone
- Sci-fi mystery
- Exploration
- Cosmic suspense
- Psychological unease

## Core Premise
Humanity receives an unknown signal from beneath the surface of Kepler-186f.

Commander Elias Ward is sent with a small expedition team to investigate.

Soon after landing, the mission discovers:
- alien ruins
- an advanced artifact
- signs that an ancient civilization once existed underground
- evidence that something may still be alive

---

# MAIN THEMES

- Curiosity vs caution
- Knowledge vs safety
- Communication vs domination
- Humanity confronting the unknown

---

# MAIN CHARACTER

## Commander Elias Ward
Role:
- Expedition leader
- Player character

Traits:
- Experienced astronaut
- Calm under pressure
- Scientific background
- Haunted by humanity's constant wars on Earth

---

# STORY STRUCTURE OVERVIEW

## Act 1 — Arrival
Player lands on Kepler and discovers the artifact.

## Act 2 — Investigation
Player explores caves and underground structures.

## Act 3 — Revelation
Player learns the fate of the alien civilization.

## Act 4 — Judgment
Player's choices determine humanity's future.

---

# SCENE FORMAT

Each scene contains:

```python
{
    "id": "001",
    "title": "Landing Site",
    "text": "Scene narrative",
    "image": "image_path.png",
    "choices": [
        ("Choice text", "next_scene_id")
    ],
    "isTerminal": False
}
```

---

# COMPLETE SCENE DATABASE

---

# SCENE 001 — LANDING SITE

## Summary
The player lands on Kepler during an electrical storm.

A strange blue pulse flashes from a partially buried alien artifact nearby.

A cave entrance can also be seen through the purple fog.

## Scene Data

```python
{
    "id": "001",
    "title": "Landing Site",
    "text": "Your ship lands violently on the rocky surface of Kepler-186f. Purple fog crawls across the ground beneath a storm-filled sky. A metallic object pulses with blue light nearby while a dark cave entrance disappears into the cliffs beyond.",
    "image": "assets/landing_site.png",
    "choices": [
        ("Touch the artifact", "002"),
        ("Scan the artifact", "003"),
        ("Ignore it and head toward the cave", "004")
    ],
    "isTerminal": False
}
```

---

# SCENE 002 — DIRECT CONTACT

## Summary
The player touches the artifact.

The artifact sends visions directly into the player's mind.

Player takes damage but receives a map leading underground.

```python
{
    "id": "002",
    "title": "Direct Contact",
    "text": "The moment your hand touches the metal surface, a surge of energy tears through your body. Your vision fractures into flashes of alien cities and collapsing stars. A map suddenly appears on your visor HUD, pointing toward a hidden underground structure.",
    "image": "assets/artifact_contact.png",
    "choices": [
        ("Follow the underground map", "005"),
        ("Return to the ship", "006")
    ],
    "isTerminal": False
}
```

---

# SCENE 003 — SCIENTIFIC ANALYSIS

## Summary
The player safely scans the artifact.

The scanner detects:
- massive energy signatures
- unknown materials
- a signal beneath the surface

Player acquires the Artifact Core.

```python
{
    "id": "003",
    "title": "Scientific Analysis",
    "text": "Your scanner emits rapid warning tones. The object contains an immense but unstable power source. Beneath the surface, faint signals pulse in response to the artifact. You carefully extract a glowing energy core from the device.",
    "image": "assets/artifact_scan.png",
    "choices": [
        ("Store the artifact safely", "007"),
        ("Track the underground signal", "005")
    ],
    "isTerminal": False
}
```

---

# SCENE 004 — THE CAVE

## Summary
The player explores the cave directly.

Inside:
- glowing alien markings
- breathing sounds
- a dormant biomechanical creature

```python
{
    "id": "004",
    "title": "The Cave",
    "text": "The cave walls glow faintly with alien symbols that pulse like veins beneath stone. Deeper inside, a massive biomechanical creature coils around a pedestal, motionless beneath layers of dust.",
    "image": "assets/cave.png",
    "choices": [
        ("Sneak past the creature", "008"),
        ("Attempt communication", "009"),
        ("Retreat quietly", "006")
    ],
    "isTerminal": False
}
```

---

# SCENE 005 — UNDERGROUND FACILITY

## Summary
The player discovers an ancient underground alien city.

Power systems begin activating.

```python
{
    "id": "005",
    "title": "Underground Facility",
    "text": "An enormous underground complex stretches beneath the planet's crust. Rows of shattered cryogenic chambers line the walls while dormant reactors hum faintly in the darkness. As you step forward, the facility begins to awaken.",
    "image": "assets/facility.png",
    "choices": [
        ("Shut down the reactor", "010"),
        ("Restore full power", "011")
    ],
    "isTerminal": False
}
```

---

# SCENE 006 — RETURN TO SHIP

## Summary
The player attempts to leave the planet.

The ship systems become infected by an unknown signal.

```python
{
    "id": "006",
    "title": "Return to Ship",
    "text": "You decide the mission has become too dangerous. But as your ship prepares for launch, every monitor flickers with strange symbols. Something from the planet has entered your systems.",
    "image": "assets/ship.png",
    "choices": [
        ("Purge the ship systems", "012"),
        ("Ignore the warnings", "013")
    ],
    "isTerminal": False
}
```

---

# SCENE 007 — SAFE CONTAINMENT

## Summary
The player safely stores the artifact.

The artifact continues emitting signals.

```python
{
    "id": "007",
    "title": "Safe Containment",
    "text": "The artifact is locked safely inside a reinforced containment unit. Yet even through the shielding, the blue glow grows stronger with every passing minute.",
    "image": "assets/containment.png",
    "choices": [
        ("Open the containment unit", "014"),
        ("Destroy the artifact", "015")
    ],
    "isTerminal": False
}
```

---

# SCENE 008 — THE TRESPASSER ENDING

```python
{
    "id": "008",
    "title": "The Trespasser",
    "text": "As you move past the creature, a loose stone cracks beneath your boot. Red eyes snap open in the darkness. Before you can react, a beam of light vaporizes you instantly.\n\n[GAME OVER — THE TRESPASSER]",
    "image": "assets/death.png",
    "choices": [
        ("Restart", "001")
    ],
    "isTerminal": True
}
```

---

# SCENE 009 — COMMUNICATION

## Summary
The creature responds peacefully.

It reveals itself as the final guardian of its civilization.

```python
{
    "id": "009",
    "title": "Communication",
    "text": "The creature slowly raises its head as your translator emits greeting signals. To your surprise, it responds calmly. It explains that its civilization destroyed itself through war and greed. 'Will humanity repeat our failure?' it asks.",
    "image": "assets/guardian.png",
    "choices": [
        ("Promise peace", "016"),
        ("Demand alien technology", "017")
    ],
    "isTerminal": False
}
```

---

# SCENE 010 — THE SILENCE ENDING

```python
{
    "id": "010",
    "title": "The Silence",
    "text": "You shut down the ancient reactor permanently. The underground city fades back into darkness. Humanity will never know what was hidden beneath Kepler-186f.\n\n[ENDING — THE SILENCE]",
    "image": "assets/silence.png",
    "choices": [
        ("Restart", "001")
    ],
    "isTerminal": True
}
```

---

# SCENE 011 — REACTIVATION

## Summary
The underground city fully powers on.

Alien defense systems activate.

```python
{
    "id": "011",
    "title": "Reactivation",
    "text": "Power floods through the underground city. Towers of blue light ignite across the darkness while massive machines awaken beneath the floor. Warning alarms echo through the facility as defense systems activate.",
    "image": "assets/reactor.png",
    "choices": [
        ("Escape immediately", "018"),
        ("Stay and investigate", "019")
    ],
    "isTerminal": False
}
```

---

# SCENE 012 — THE SURVIVOR ENDING

```python
{
    "id": "012",
    "title": "The Survivor",
    "text": "You destroy the infected ship systems before the signal can spread further. The journey home is nearly fatal, but you survive. Humanity never learns the truth about Kepler-186f.\n\n[ENDING — THE SURVIVOR]",
    "image": "assets/survivor.png",
    "choices": [
        ("Restart", "001")
    ],
    "isTerminal": True
}
```

---

# SCENE 013 — THE SIGNAL ENDING

```python
{
    "id": "013",
    "title": "The Signal",
    "text": "The strange signal spreads silently through your ship systems during the return journey. By the time you reach Earth, it has already infiltrated global networks. Humanity never notices the invasion beginning.\n\n[ENDING — THE SIGNAL]",
    "image": "assets/signal.png",
    "choices": [
        ("Restart", "001")
    ],
    "isTerminal": True
}
```

---

# SCENE 014 — ALIEN MEMORIES

## Summary
The artifact fully activates.

The player experiences memories from the extinct civilization.

```python
{
    "id": "014",
    "title": "Alien Memories",
    "text": "The containment unit opens and blue light floods the room. Suddenly you experience the memories of an alien civilization: towering cities, peaceful oceans, and finally total destruction through endless war.",
    "image": "assets/memories.png",
    "choices": [
        ("Share the knowledge with Earth", "020"),
        ("Keep the truth secret", "021")
    ],
    "isTerminal": False
}
```

---

# SCENE 015 — THE FOOL ENDING

```python
{
    "id": "015",
    "title": "The Fool",
    "text": "You attempt to destroy the artifact. The core destabilizes instantly and erupts in a violent explosion that consumes the entire chamber.\n\n[ENDING — THE FOOL]",
    "image": "assets/explosion.png",
    "choices": [
        ("Restart", "001")
    ],
    "isTerminal": True
}
```

---

# SCENE 016 — THE DIPLOMAT ENDING

```python
{
    "id": "016",
    "title": "The Diplomat",
    "text": "The guardian studies you silently before granting humanity advanced medicine and clean energy technology. Humanity is judged worthy of inheriting the knowledge of a fallen civilization.\n\n[TRUE ENDING — THE DIPLOMAT]",
    "image": "assets/diplomat.png",
    "choices": [
        ("Restart", "001")
    ],
    "isTerminal": True
}
```

---

# SCENE 017 — THE CONQUEROR ENDING

```python
{
    "id": "017",
    "title": "The Conqueror",
    "text": "The guardian's eyes burn red as it realizes humanity seeks power rather than understanding. Ancient defense systems awaken beneath the planet and erase your expedition completely.\n\n[ENDING — THE CONQUEROR]",
    "image": "assets/conqueror.png",
    "choices": [
        ("Restart", "001")
    ],
    "isTerminal": True
}
```

---

# SCENE 018 — THE ESCAPEE ENDING

```python
{
    "id": "018",
    "title": "The Escapee",
    "text": "You flee the collapsing underground city just before the ancient systems overload. Earth celebrates you as a hero, but you can never forget what still sleeps beneath Kepler-186f.\n\n[ENDING — THE ESCAPEE]",
    "image": "assets/escape.png",
    "choices": [
        ("Restart", "001")
    ],
    "isTerminal": True
}
```

---

# SCENE 019 — THE ARCHIVIST ENDING

```python
{
    "id": "019",
    "title": "The Archivist",
    "text": "You remain inside the awakened city and discover preserved alien consciousnesses stored within an immense archive. Choosing knowledge over mortality, you upload your own mind into the system forever.\n\n[SECRET ENDING — THE ARCHIVIST]",
    "image": "assets/archive.png",
    "choices": [
        ("Restart", "001")
    ],
    "isTerminal": True
}
```

---

# SCENE 020 — THE RENAISSANCE ENDING

```python
{
    "id": "020",
    "title": "The Renaissance",
    "text": "Humanity unites around the knowledge recovered from Kepler-186f. Disease, famine, and energy shortages disappear within decades as civilization enters a new golden age.\n\n[ENDING — THE RENAISSANCE]",
    "image": "assets/renaissance.png",
    "choices": [
        ("Restart", "001")
    ],
    "isTerminal": True
}
```

---

# SCENE 021 — THE KEEPER ENDING

```python
{
    "id": "021",
    "title": "The Keeper",
    "text": "You hide the truth about the artifact from the world. Governments and corporations hunt you endlessly while the blue glow of the artifact continues pulsing in the darkness beside you.\n\n[ENDING — THE KEEPER]",
    "image": "assets/keeper.png",
    "choices": [
        ("Restart", "001")
    ],
    "isTerminal": True
}
```

---

# IMPLEMENTATION NOTES

## Current Compatible Features

The structure already supports:
- scene-based navigation
- image switching
- multiple endings
- branching paths
- restart loops

---

# FUTURE EXPANSION OPTIONS

Later systems can add:

## Inventory
Example:

```python
"Has_Artifact": True
```

## Health
Example:

```python
"Player_Health": 80
```

## Hidden Morality
Example:

```python
"Empathy": 5
```

## Conditional Choices
Example:

```python
"requirements": {
    "Has_Artifact": True
}
```

## Companion Characters
Possible future crew members:
- scientist
- soldier
- AI assistant
- rival explorer

## Expanded Planet Exploration
Additional areas:
- alien city
- crashed ship
- ocean ruins
- orbital station
- abandoned laboratories

---

# FINAL DESIGN GOAL

This structure should serve as:
- the game's narrative backbone
- a machine-readable story framework
- a scalable branching narrative foundation

It is intentionally simple enough for manual implementation while remaining expandable into larger systems later.

