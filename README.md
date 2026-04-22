# Open Design and Technology  
## Final Project README

> **Project Weight:** 70%  
> **Team Size:** 2 students  
> **Project Duration:** 4 weeks  
> **Class Time Available:** 6 hours per class  
> **Total Time Available:** 48 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository
After forking this repository, rename it using the format:

`ODT-2026-TeamName`

### Example
`ODT-2026-PixelWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the 4-week build period.  
By the final review, this README should clearly show:
- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules
- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 Studio / Group Name
`[Laser Light]`

## 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| `[Garima]` | `[Coding, mechanics]` | `[App building and connection]` | `[Mathematical logic,Coding,system integration]` |
| `[Janhavi]` | `[App building and connection , mechanics]` | `[Coding]` | `[Analytical thinking,mathematical logic, App making,problem solving]` |

## 1.3 Project Title
`[Laser light Painting machine.]`

## 1.4 One-Line Pitch
`[This project demonstrates how a laser and servos can work together to turn simple code into precise visual art.]`

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
`[This project is a laser light painting machine where a user draws a simple sketch on their phone, and that drawing is then recreated on a wall using a laser mounted on two servo motors. An ESP32 translates the drawing into motion, guiding the laser to trace it point by point. While the laser is moving, you only see a single dot traveling across the surface,but when captured using a long-exposure photograph, the full drawing appears as a continuous glowing image.
]`

---

# 2. Philosophy Fit

## 2.1 Experience, Not Social Problem
This module does **not** require your project to solve a large social problem.

You are allowed to build:
- toys,
- games,
- interactive objects,
- playful machines,
- kinetic artifacts,
- humorous devices,
- strange but delightful experiences,
- things that are entertaining to use or watch.

## 2.2 What kind of experience are you creating?
Answer the following:
- What is the experience?
- What do you want the player or participant to feel?
- Why would someone want to try it again?

**Response:**  
`[-The user creates a digital sketch on their phone, which is then physically recreated by a laser mounted on servo motors via an ESP32 . As the laser traces the drawing on a wall in real time, the user captures it using a long-exposure photograph. The final output isn’t just the drawing,it’s a glowing, continuous light trail captured through the camera, revealing a version of the artwork that isn’t visible to the naked eye in one instant.
 
 -A sense of anticipation and reveal. Unlike normal drawing, the result isn’t immediately visible,you only fully see it after taking the long-exposure shot. This creates a feeling  surprise. There’s also a sense of translation : something drawn digitally becomes a physical, and then becomes a photographic artifact. It should feel a bit like capturing something invisible or hidden
 
 -People will want to tweak their drawing, try different shapes, or play with camera settings to get a cooler result. Even small changes can make the photo look completely different. Also, since you end up with a photo each time, it becomes something you’d want to improve, share, or experiment with again and again.]`

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
`[We are designing this project as if we are a small creative studio making an interactive experience for a mixed audience of classmates and exhibition visitors.]`

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| `[Video]` | `[https://www.instagram.com/reel/DWbnYinCgSN/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==]` | `[Inspired the idea of translating digital drawings into physical light-based visuals ]` |

## 3.2 Original Twist
What makes your project original?

**Response:**  
`[What makes our project original is the way we approach control and interaction. Instead of manual control, the system uses a mobile app interface where users can draw freely and have their input translated automatically into motion.Using an ESP32 with a pan tilt servo mechanism, the system interprets drawing data and recreates it on the wall. This shifts the experience from simply controlling movement to creating drawings, making it more expressive and accessible.
The addition of longe xposure capture adds another layer, where the final image is only revealed after the motion is complete]`

---

# 4. Project Intent

## 4.1 Core Interaction Loop
Describe the main loop of interaction.

Examples:
- press → launch → score → reset
- connect → control → observe → repeat
- turn → trigger → react → repeat
- move object → sensor detects → sound/light response → player reacts

**Response:**  
`[draw image on phone → send to ESP via Bluetooth → ESP converts to motion → laser traces drawing on wall → user captures long-exposure photo → view result → modify and resend → repeat]`

## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? | `[Design students, curious creators, and exhibition visitors interested in interactive art and tech]` |
| Age range | `[all ages]` |
| Solo or multiplayer | `[Primarily solo, but others can observe or take turns]` |
| Expected duration of one round | `[1-2 minutes]` |
| What should the player feel? | `[Curious, excited, and satisfied—,specially during the final reveal of the long-exposure image]` |
| Is explanation required before use? | `[Yes, a brief explanation is needed]` |

## 4.3 Player Journey
Describe exactly how a player will use the project.

1. **Approach:** `[The player sees a laser setup aimed at a wall along with a phone interface. A camera is already positioned, hinting that something is being captured.]`
2. **Start:** `[They pick up the phone and connect to the system via Bluetooth]`
3. **First Action:** `[The player draws a simple sketch or pattern on the phone screen]`
4. **Main Interaction:** `[They send the drawing, and the laser begins tracing it on the wall. While this happens, the camera automatically captures the motion as a long-exposure image.]`
5. **System Response:** `[The system translates the drawing into coordinated servo movements, guiding the laser to recreate the sketch. The moving dot is visible in real time, while the camera records the full light path]`
6. **Win / Lose / End Condition:** `[The round ends when the laser finishes tracing and the captured image is revealed. There’s no win or lose,the outcome is judged by how visually satisfying or interesting the result is.]`
7. **Reset:** `[The player clears or edits their drawing on the phone and sends a new one, starting the next round immediately]`

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

- `[N/A (Not Applicable as a traditional game)

This project does not function as a rule-based or competitive game with defined win/lose conditions. Instead, it is an open-ended interactive experience focused on exploration and creativity. The user is free to draw anything, experiment with different patterns, and interpret the results in their own way. There are no strict objectives, constraints, or scoring systems]`


---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

- [1] `[The user is able to successfully connect the phone to the system via Bluetooth without repeated failures.]`
- [2] `[The user can draw an image on the phone and send it to the system, and the data is received correctly by the microcontroller]`
- [3] `[The system accurately translates the drawing into motion, and the laser traces the image clearly on the wall using the servo mechanism.]`
- [4] `[he camera setup consistently captures the full light path as a long-exposure image, allowing the final drawing to be visible.]`
- [5] `[he entire interaction loop  can be completed smoothly and repeated without major technical interruptions]`

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
`[In the current version the user has the liberty to draw whatever they please.
The minimum viable version would be where the user is given a predefined list of shapes/drawings that they can select from, to draw on the wall with the help of the laser.]`

## 5.3 Stretch Features
What features are nice to have but not essential?

- `[Adding the undo and redo option in the app.]`
- `[Adding various colour lasers  ]`
- `[option to adjust stroke thickness]`

---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [Yes] Electronics-based
- [Yes] Mechanical
- [ ] Sensor-based
- [Yes] App-connected
- [Yes] Motorized
- [ ] Sound-based
- [Yes] Light-based
- [Yes] Screen/UI-based
- [Yes] Fabricated structure
- [ ] Game logic based
- [ ] Installation / tabletop experience
- [ ] Other: `[Write here]`

## 6.2 High-Level System Description
Explain how the system works in simple terms.

Include:
- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Response:**  
`[Input-The user draws a sketch on a mobile app. This drawing is captured as a set of coordinates and sent to the system via Bluetooth.

  Processing-An ESP32 receives this data and processes it by converting the coordinates into movement instructions. It calculates how the two servo motors need to   move in order to recreate the drawing.
  
  Output: A laser module, mounted on the servos, traces the drawing on a wall. While only a moving dot is visible in real time, a pre-set camera captures the        motion as a    long-exposure image, revealing the full drawing.
  
  Physical Structure:
  The system consists of a base holding two servo motors arranged to control movement in two axes (X and Y), with a laser attached to the moving mechanism. The      setup is positioned facing a wall, and a camera is fixed in place to capture the output
  
  App Interaction:
  The mobile app acts as the main interface where the user draws and sends the image. It also controls when the system starts tracing, making the interaction        simple and direct.]`

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| `[Mobile App (Drawing Interface)]` | Input | `[Allows the user to draw an image and sends the coordinate data to the system via Bluetooth]` |
| `[ESP32]` | Processing | `[Receives the drawing data, processes it into movement instructions, and controls the servo motors accordingly]` |
| `[Servo Motors + laser Module]` | Output | `[The servos move in X and Y directions to guide the laser, which traces the drawing on the wall]` |
| `[Mechanical Assembly(Servo Mount + Laser holder]` | Physical Action | `[Holds and aligns the servos and laser, enabling controlled 2D movement to recreate the drawing accurately]` |

---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

**Insert image below:**  
`[<img width="902" height="1600" alt="image" src="https://github.com/user-attachments/assets/7729b553-84e2-4986-85f6-3b76d864dd1f" />
]`

Example:
```md

```

## 7.2 Labeled Build Sketch
Add a sketch with labels showing:
- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
`[Upload image and link here]`

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | `[10cm]` |
| Width | `[6cm]` |
| Height | `[12cm]` |
| Estimated weight | `[30grams]` |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [ ] Gears
- [ ] Pulleys
- [ ] Belt drives
- [ ] Linkages
- [ ] Hinges
- [ ] Shafts
- [ ] Springs
- [ ] Bearings
- [ ] Wheels
- [ ] Sliders
- [ ] Levers
- [Yes ] Not applicable

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
`[The mechanism consists of two servo motors arranged to control movement along two axes (horizontal and vertical), with a laser module attached to the moving part. This setup works like a simple plotter: one servo controls left–right movement, while the other controls up–down movement. Together, they allow the laser to be positioned at different points on a wall.

An ESP32 sends precise angle signals to each servo, guiding the laser step by step along a path. As the servos move, the laser traces the exact coordinates of the drawing provided by the user. The purpose of this mechanism is to convert a digital sketch into a physical motion, enabling the laser to draw the image in real space, which can then be captured as a complete light painting using long-exposure photography.]`

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
`[What moves:
  A laser module mounted on a two axis mechanism(The pan tilt mechanism) moves across the wall. This motion is controlled by two servo motors; one handling horizontal (X-axis) movement     and the other vertical (Y-axis).
  What causes the movement:
  An ESP32 sends PWM signals to the servos based on the coordinates received from the mobile app. These signals determine the angle and direction of each servo,     resulting in controlled movement of the laser.
  How far it moves:
  The movement range depends on the servo rotation limits (typically around 0° to 180°). This translates to a defined drawing area on the wall, mapped from the      phone screen to the physical space.
  How fast it moves:
  The speed is controlled programmatically by adjusting the delay between position updates. It is kept slow and steady so the laser can clearly trace the path and   be captured effectively in a long-exposure image.
  What could go wrong:
  The movement may become inaccurate due to servo jitter, poor calibration, or incorrect mapping of coordinates. Power fluctuations can cause unstable motion, and   sudden or fast movements may distort the drawing. Additionally, communication delays or disconnections can interrupt the motion mid way.]`

## 8.4 Simulation / CAD / Animation Before Making
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| `[Fusion 360 / Tinkercad / other]` | `[Link or screenshot]` | `[What did you validate?]` |
| `[Tool]` | `[Link or screenshot]` | `[What did you validate?]` |

## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
`[NA]`

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|---|---:|---|
| `[ESP32]` | `1` | `[Main controller that receives data from the app and controls the system]` |
| `[Servo Motor]` | `[2]` | `[Controls movement along X and Y axes to position the laser]` |
| `[Laser Module]` | `[1]` | `[Traces the drawing on the wall based on data received from the app]` |
| `[Power supply]` | `[1]` | `[Provides stable power to the ESP32 and servo motors]` |
| `[Jumper wires]` | `[Multiple]` | `[Connects all the electrical components together]` |


## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
`[The ESP32 is connected to two servo motors, each with three wires: 5V, GND, and signal. The signal wires from both servos are connected to separate PWM-capable GPIO pins on the ESP32, allowing control of movement along the X and Y axes. The servos are powered using an external 5V power supply, and their ground is connected to the ESP32 ground to ensure a common reference.

The laser module is directly connected to the power supply (5V and GND), so it remains continuously ON during operation. It is mounted onto the servo mechanism, and its movement is controlled indirectly through the motion of the servos rather than through any electronic control signal.]`

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[<img width="900" height="1600" alt="image" src="https://github.com/user-attachments/assets/f19fa7b5-3765-4bce-bdc7-643ab27e292c" />
]`

## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | `[Adapter (external 5V supply) + USB]` |
| Voltage required | `[5V for servo motors and laser module; 5V (USB) for the ESP32]` |
| Current concerns | `[Servo motors can draw high current, causing voltage drops or unstable performance if not powered separately]` |
| Safety concerns | `[Ensuring common ground, avoid short circuits, preventing overheating(using buck converter), and avoid direct exposure to the laser beam]` |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| `[Micropython]` | `[Programs the ESP32 to process incoming data and control servo movement]` |
| `[MIT App inventor]` | `[Used to build the mobile app for drawing and sending data via Bluetooth]` |
| `[nRF Connect]` | `[Used to test and debug BLE communication between the phone and ESP32]` |

## 10.2 Software Logic
Describe what the code must do.

Include:
- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
`[Startup behavior:
When powered on, the ESP32 initializes Bluetooth communication, sets up GPIO pins for the servo motors, and moves the servos to a default  position. It then begins advertising for a connection from the mobile app.
Input handling:
The system receives drawing data (a sequence of X–Y coordinates) from the mobile app via Bluetooth. This data is stored temporarily and prepared for execution.
Sensor reading:
No sensors are used in this system, so this step is not applicable.
Decision logic:
The ESP32 interprets the incoming coordinates and maps them to corresponding servo angles. It determines the sequence of movements required to recreate the drawing smoothly and in order.
Output behavior:
The ESP32 sends  signals to the two servo motors, controlling their angles step by step so that the laser traces the drawing on the wall.
Communication logic:
Bluetooth Low Energy (BLE) is used to establish a connection with the app. The ESP32 receives data through specific services and characteristics, ensuring reliable transmission of drawing coordinates.
Reset behavior:
After completing one drawing, the system either returns the servos to the starting position or waits for new input. The user can send a new drawing to begin the next cycle without restarting the system.]`

## 10.3 Code Flowchart
Insert a flowchart showing your code logic.

Suggested sequence:
- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
`[Upload image and link here]`

## 10.4 Pseudocode

```text
[Write your pseudocode here]
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [Yes] Yes
- [ ] No

If yes, complete this section.

## 11.2 Why is the app needed?
Explain what the app adds to the experience.

Examples:
- remote control,
- score tracking,
- mode selection,
- personalization,
- triggering effects,
- displaying data.

**Response:**  
`[the app turns the system from a mechanism to an interative experience.The app allows the user to draw freely on the screen, which becomes the input for the system. Instead of manually controlling motors or entering coordinates, the user can  sketch shapes, patterns, or symbols. It also enables wireless control via Bluetooth, sending the drawing data directly to the ESP32. This removes the need for physical connections and makes the experience more seamless and engaging.
Overall, the app adds:

Personalization → every user creates their own unique light painting
Ease of interaction → no technical knowledge needed
Control and flexibility → start, stop, reset anytime
Playfulness → turns a technical setup into a creative tool]'

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `[scan]` | `[scans for available devices]` |
| `[select a device]` | `[Allows the user to browse available Bluetooth devices, select one, and establish a connection]` |
| `[clear]` | `[Allows the user to clear the drawing they have made]` |
| `[send]` | `[Sends the completed drawing to the system so the laser can trace it on the wall]` |
| `[origin]` | `[Sends the laser back to its starting position]` |
| `[status label]` | `[Displays connection status]` |
| `[canvas]` | `[Provides the user with a space to freely draw shapes, patterns, or symbols for the laser to trace.]` |

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 App Screen Flow

1. `[Click on the scan button]`
2. `[When the label shows "scanning" click on select a device]`
3. `[Choose ESP32 BLE name form the device list]`
4. `[when the label reads connected set to origin]`
5. `[draw on the canvas]`
6. `[after the drawing is completed click on send.]`
7. `[The system begins tracing the drawing with the laser on the wall.]`
8. `[The user can clear the canvas to repeat the process..]`
---

# 12. Bill of Materials

## 12.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| `[ESP32]` | `1` | `Yes` | `No` | `0` | `[WROOM]` | `[As a microcontroller for the project]` |
| `[Servo]` | `[2]` | `[Yes]` | `[No]` | `[Cost]` | `[SG90]` | `[For precise movement]` |
| `[laser]` | `[1]` | `[Yes]` | `[No]` | `[Cost]` | `[Laser module]` | `[Gives a precise point and is small and easy to connect]` |
| `[power module]` | `[1]` | `[Yes]` | `[No]` | `[Cost]` | `[Spec]` | `[]` |
| `[wires]` | `[multiple]` | `[yes]` | `[No]` | `[Cost]` | `[Jumper wires as well as normal wires]` | `[Jumper wires are easy to connect to a breadboard and give definite connection]` |

## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
`[We chose to use 3D printed parts for the structure because they allow for precise  iteration. Since the mechanism requires accurate alignment of the servos and the laser, 3D printing makes it possible to design parts that fit perfectly. Compared to materials like cardboard or MDF, it provides better stability and a cleaner, more reliable build.

We used servo motors instead of DC motors because servos allow for precise control over position and angle. This is essential for accurately tracing drawings, as the system needs to move to specific coordinates rather than just rotate continuously. Servos make it much easier to control movement along the X and Y axes.

A laser module was chosen instead of an LED because it produces a focused and sharp beam of light. This is important for creating clear and defined light trails, especially when captured using long-exposure photography. An LED would produce a more diffused light, resulting in less precise drawings.]`

## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| `[N/A]` | `[N/A]` | `[N/A]` | `[N/A]` | `[N/A]` |

## 12.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---:|
| Electronics | `[N/A]` |
| Mechanical parts | `[N/A]` |
| Fabrication materials | `[N/A]` |
| Purchased extras | `[N/A]` |
| Contingency | `[N/A]` |
| **Total** | `[N/A]` |

## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
`[N/A]`

---

# 13. Planning the Work

## 13.1 Team Working Agreement
Write how your team will work together.

Include:
- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  
`[Write here]`

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---:|---|---|---|
| T1 | `[Finalize concept]` | `[Both]` | `2` | `[6.4.26]` | `None` | `Done` |
| T2 | `[Complete BOM]` | `[Both]` | `1` | `[5.4.26]` | `T1` | `Done` |
| T3 | `[Test electronics]` | `[Janhavi]` | `2` | `[8.4.26]` | `T1` | `Done` |
| T4 | `[Build structure]` | `[Janhavi]` | `4` | `[15.4.26]` | `T1` | `Done` |
| T5 | `[Write control code]` | `[Garima]` | `4` | `[15.4.26]` | `T3` | `Done` |
| T6 | `[Integrate system]` | `[Janhavi]` | `4` | `[17.4.26]` | `T4, T5` | `Done` |
| T7 | `[Playtest]` | `[Both]` | `2` | `[Date]` | `19.4.26` | `Done` |
| T8 | `[Refine and document]` | `[Garima]` | `3` | `[20.4.26]` | `T7` | `Done` |

## 13.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept and gameplay | `[Both]` | `[Both]` |
| Electronics | `[Garima]` | `[Janhavi]` |
| Coding | `[Garima]` | `[Janhavi]` |
| App | `[Janhavi]` | `[Garima]` |
| Mechanical build | `[Janhavi]` | `[Garima]` |
| Testing | `[Janhavi]` | `[Garima]` |
| Documentation | `[Garima]` | `[Janhavi]` |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [Yes] Idea finalized
- [Yes] Core interaction decided
- [Yes] Sketches made
- [Yes ] BOM completed
- [Yes] Purchase needs identified
- [Yes] Key uncertainty identified
- [Yes] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [Yes] Electronics tests completed
- [No] CAD / structure planning completed
- [No] App UI started if needed
- [Yes] Mechanical concept tested
- [No] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [Yes] Physical body built
- [Yes] Electronics integrated
- [Yes] Code connected to hardware
- [Yes] App connected if required
- [Yes] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [Yes] Technical bugs reduced
- [No] Playtesting completed
- [Yes] Improvements made
- [No] Documentation completed
- [Yes] Final build ready

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | `[Finalize concept, figure out working]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 2 | `[Finalize working, electronic components, mechanical structure, start code]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 3 | `[Complete code, complete app, complete structure, integrate together and test]` | `[Code completed, structure completed, app completed, integration started but not complete, testing remaining]` | `[App completed but not able to test as esp stopped working hence had to buy a new one]` | `[Complete backlog and catchup with goals]` |
| Week 4 | `[Debugging and final refinement]` | `[Write here]` | `[Write here]` | `[Write here]` |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| `[Bluetooth disconnects]` | `Technical` | `Medium` | `High` | `[Fallback interaction /simplify connection flow]` | `[Janhavi]` |
| `[Structure breaks during play]` | `Mechanical` | `Medium` | `High` | `[Reinforce joints / change material]` | `[Name]` |
| `[Risk]` | `[Technical / Material / Time / Gameplay]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |
| `[Risk]` | `[Type]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |

## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
`[The biggest uncertainty is the reliability of Bluetooth communication between the app (built using MIT App Inventor) and the ESP32]`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| `[Bluetooth connection]` | `[Attempt to connect the app to the ESP32]` | `[App connects within a few seconds every time and stays connected]` |
| `[Mechanism movement]` | `[Try to draw simple shapes staring from a line and sqaure, without connecting to app]` | `[Getting clean lines which fairly resemble intended shape without too much distortion]` |
| `[App communication]` | `[Checking if the app is sending coordinates of drawings to the esp]` | `[App sending proper coordinates]` |

## 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Do players understand what to do? | `[Observe users interacting with the system with minimal instructions and check if they can connect, draw, and send the drawing correctly]` |
| Is the interaction satisfying? | `[Ask users for feedback and observe their reaction when they see the final light painting]` |
| Do players want another turn? | `[Check if users voluntarily try again or experiment with new drawings after their first attempt]` |
| Is the challenge balanced? | `[Observe if users are able to create recognizable shapes without frustration]` |
| Is the response clear and immediate? | `[Monitor if the laser starts tracing soon after sending the drawing and if the system responds without noticeable delay or confusion]` |

## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| `[Date]` | `[Describe issue]` | `[Technical / Mechanical / UI / Gameplay]` | `[What you did]` | `[Worked / Partly / Failed]` | `[Next step]` |
| `[Date]` | `[Describe issue]` | `[Type]` | `[What you did]` | `[Result]` | `[Next step]` |

## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |

---

# 17. Build Documentation

## 17.1 Fabrication Process
Describe how the project was physically made.

Include:
- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
`[Write here]`

## 17.2 Build Photos
Add photos throughout the project.

Suggested images:
- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.

Example:
```md



```

## 17.3 Version History

| Version | Date | What Changed | Why |
|---|---|---|---|
| `v1` | `[16.4.26]` | `[Changed material from mdf to 3d printing]` | `[3d printing allows for a better form for the structure with precise slots and indentations for components leading to a better fit.]` |

---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
`[the final version is a laser light painting machine where users draw on a mobile app (built using MIT App Inventor) and send their drawing via Bluetooth to an ESP32. The ESP32 controls two servo motors (along the x and y axes) that move a laser to trace the drawing on a wall .A fixed camera captures the motion as a long-exposure image, revealing the complete light drawing]`

## 18.2 What Works Well
- `[Focused beam of the laser gives clear and precise lines]`
- `[Servo motors provide controlled and accurate movement for tracing shapes]`
- `[Simple App interaction makes it easy for the user to draw the image]`

## 18.3 What Still Needs Improvement
- `[Smoothness in movement of the motors]`
- `[Speed at which the servos will complete the drawing still a bit unpredictable]`
- `[Accuracy in copying the image from the user input]`

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`[We initially planned real-time drawing transmission ( The x and y coordinates would be sent continuously), but switched to sending the full drawing after completion for better stability. We also restricted servo angles to keep the laser on the wall and refined the motion for smoother, more accurate tracing.]`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`[We worked well in breaking down the project into parts (app, hardware, and mechanism)., especially with Bluetooth and movement. We were able to adapt quickly when something didn’t work and find practical solutions.]`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`[Through this project, we understood how electronics can actually control physical movement and create something interactive. Working with the ESP32 made it clear how code directly translates into real-world motion. While coding in MicroPython, we learned how logic, data flow, and communication really affect how the system behaves. It was interesting to see how the same hardware can give completely different results just based on how it’s programmed.
For the mechanism, we got a better understanding of how a pan-tilt setup works and how important precise control is for getting accurate drawings.
Using 3D printing also showed us how important proper alignment and structure are small errors in the build can affect the entire output.
Overall, the biggest learning was how everything connects. Electronics, coding, and the physical setup all depend on each other, and even a small issue in one part can affect the whole system.]`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`[This project helped us understand that designing for play is less about adding features and more about shaping a clear and engaging experience. The core loop, drawing, sending, and watching became meaningful because it included a sense of anticipation and reveal. That moment where the final image appears created a subtle sense of delight, showing us how timing and outcome can strongly influence engagement. We also learned that clarity in interaction is critical, and that starting with a simple, direct system worked in our favor. Since the interaction was always straightforward (draw → send → observe), users were able to understand it immediately without confusion. This showed us that keeping the interaction minimal from the beginning can be more effective than adding extra features or controls.In terms of player understanding, we saw how important feedback and consistency are. If the system responds in a stable and expected way, users quickly build trust and start experimenting more freely. Finally, iteration played a major role. Many of our early ideas didn’t work as expected, especially with real-time data and connectivity. Each change forced us to rethink both the technical and interaction design. Over time, we moved toward a simpler and more reliable system, showing that refining and simplifying is often more valuable than adding complexity.
]`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`[We would improve the smoothness and accuracy of the laser movement so that drawings look cleaner and more precise
 On the app side (built using MIT App Inventor), we would enhance the interface by adding features like adjustable brush size, undo options.]`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [Yes ] Team details are complete
- [Yes ] Project description is complete
- [Yes ] Inspiration sources are included
- [Yes ] Player journey is written
- [yes ] Sketches are added
- [Yes ] BOM is complete
- [Yes] Purchase list is complete
- [Yes ] Budget summary is complete
- [Yes ] Mechanical planning is documented if applicable
- [Yes ] App planning is documented if applicable
- [ Yes] Code flowchart is added
- [Yes ] Task breakdown is complete
- [ Yes] Weekly logs are updated
- [Yes ] Risk register is complete
- [Yes ] Testing log is updated
- [ Yes] Playtesting notes are included
- [Yes ] Build photos are included
- [Yes ] Final reflection is written

---

# 21. Suggested Repository Structure

```text
project-repo/
├── README.md
├── images/
│   ├── concept-sketch.jpg
│   ├── labeled-sketch.jpg
│   ├── circuit-diagram.jpg
│   ├── ui-mockup.jpg
│   ├── prototype-1.jpg
│   └── final-build.jpg
├── code/
│   ├── main.py
│   ├── test_code.py
│   └── notes.md
├── cad/
│   ├── models/
│   └── screenshots/
└── docs/
    ├── references.md
    └── extra-notes.md
```

---

# 22. Instructor Review

## 22.1 Proposal Approval
- [ ] Approved to proceed
- [ ] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review
`[Instructor fills this section]`

## 22.3 Final Review Notes
`[Instructor fills this section]`
