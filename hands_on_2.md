# Exercise 2: Connect the Canva MCP Server (Remote MCP Server)

## Objective

By the end of this exercise, participants will connect the **Canva MCP remote server** to an MCP-compatible AI client (Claude), authenticate with Canva, and use AI to **create, edit, and retrieve Canva designs** using natural language.

---

## ⏱️ Time

**20–30 minutes**

---

## Background (Why this matters)

In Exercise 1, you connected a **local MCP server**.
In this exercise, you’ll connect a **remote MCP server hosted by Canva**.

The Canva MCP server enables AI-driven design workflows such as:

* Creating presentations, posters, or social media posts
* Editing existing designs
* Exporting brand-aligned assets
* Automating repetitive design tasks

This demonstrates how MCP enables **real-world creative and business workflows** powered by AI.

---

## Prerequisites

Before starting, ensure:

* An active Canva account (Free or Pro)
* Access to Claude with **Connectors / MCP support enabled**
* Ability to authenticate via Canva OAuth
* Stable internet connection

**Important:**
Participants should be logged into the correct Canva account before beginning.

---

## Security Note (Read Aloud)

> The Canva MCP server uses OAuth authentication.
> You will explicitly approve which Canva resources the assistant can access.
> Access can be revoked anytime from Canva account settings.

---

## Step-by-Step Instructions

---

### Step 1: Open Connector Settings in Claude

1. Open **Claude (web version)**
2. Click your **profile icon**
3. Select **Settings**
4. Navigate to **Connectors**

You will see your existing and available MCP connections.

---

### Step 2: Add the Canva MCP Server

1. Click **Add custom connector**
2. Enter the Canva MCP server URL:

```
https://mcp.canva.com
```

3. Click **Add**

Claude will attempt to establish a connection.

---

### Step 3: Authenticate with Canva

1. You’ll be redirected to Canva
2. Log in (if not already)
3. Review requested permissions (design creation, editing, file access)
4. Click **Allow**

Once successful, you’ll return to Claude with the **Canva MCP server connected**.

---

### Step 4: Review Available Canva Tools

1. In **Settings → Connectors**
2. Click **Canva MCP Server**
3. Review available tools such as:

   * Create new design
   * Edit existing design
   * Export design
   * Access brand kits (if enabled)

---

## Hands-On Tasks

Participants should now try the following prompts.

---

### Task 1: Create a New Design

Ask Claude:
> “Create a clean LinkedIn post design announcing an upcoming AI workshop.”

Approve the design creation request when prompted.

---

### Task 2: Modify an Existing Design

Ask Claude:

> “Update the design to use a blue and white color palette and make the headline more bold.”

Observe how Claude applies design changes.

---

### Task 3: Generate a Presentation Slide

Ask Claude:

> “Create a single presentation slide titled ‘What is MCP?’ with icons and minimal text.”

---

### Task 4 (Optional – Advanced)

Ask Claude:

> “Adapt this design to follow Canva’s modern corporate style and export it as a PNG.”

---

## Permissions Checkpoint

For each action:

* Claude requests **explicit approval**
* Permissions are **scoped to Canva actions**
* No design changes occur without user consent

**Key Concept:**
MCP ensures *creative automation without losing human control*.

---

## Troubleshooting

If the Canva MCP server does not connect:

* Ensure pop-ups are enabled
* Confirm you’re logged into the correct Canva account
* Remove and re-add the connector
* Retry OAuth authentication

If a design action fails:

* Verify the tool is enabled in Connector settings
* Check Canva permissions and workspace access

---

## Completion Criteria

Participants should be able to confirm:

* [ ] Canva MCP server is connected
* [ ] OAuth authentication completed successfully
* [ ] New designs can be created via AI
* [ ] Existing designs can be edited
* [ ] Exports are generated
* [ ] Permissions are visible and controllable

---

## Reflection Questions (Discussion)

1. How does Canva MCP differ from manually designing in Canva?
2. What design tasks could be fully automated using MCP?
3. Where should human creativity remain essential?
4. How could this integrate into marketing or content teams?

---

## Transition to Next Exercise

> *“We’ve now connected local tools, productivity platforms, and creative systems. Next, we’ll learn how to **build our own MCP server** and expose custom tools to an AI agent.”*



---
