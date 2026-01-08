# Exercise 1: Connect a Local MCP Server (Filesystem)

## Objective

By the end of this exercise, participants will successfully connect a **local filesystem MCP server** to Claude Desktop and perform basic file operations with explicit user approval.

---

## Time

**20–25 minutes**

---

## Prerequisites

Ensure the following are ready **before starting**:

* Claude Desktop (latest version)
* Node.js installed
  Verify by running:

  ```bash
  node --version
  ```
* Access to your local Desktop or Downloads folder

---

## Background (Why this matters)

The Model Context Protocol (MCP) allows AI clients like Claude Desktop to interact with **local tools** in a secure, permission-based way. In this exercise, you will expose your local filesystem as a tool that Claude can request access to—demonstrating real-world agent capabilities.

---

## 🛠️ Step-by-Step Instructions

### Step 1: Open Claude Desktop Configuration

1. Open **Claude Desktop**
2. From the menu bar, select **Settings**
3. Navigate to **Developer → Edit Config**
4. Open the configuration file (`claude_desktop_config.json`)

> If the file does not exist, Claude will create it automatically.

---

### Step 2: Add the Filesystem MCP Server

Paste the following configuration into the file.

Replace `YOUR_USERNAME` with your system username.

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/YOUR_USERNAME/Desktop",
        "/Users/YOUR_USERNAME/Downloads"
      ]
    }
  }
}
```

---

### Step 3: Restart Claude Desktop

* Completely quit Claude Desktop
* Reopen the application

Success indicator:
You should see an MCP/tool indicator near the chat input area.

---

## 🧪 Hands-On Tasks

Ask Claude to perform each of the following:

### Task 1: Create a File

> “Create a short motivational quote and save it as `workshop.txt` on my Desktop.”

Approve the action when prompted.

---

### Task 2: Read Files

> “List all files currently on my Desktop.”

---

### Task 3: Organize Files

> “Create a folder called `Workshop` on my Desktop and move `workshop.txt` into it.”

---

## Permission Checkpoint

For every filesystem action:

* Claude will request **explicit approval**
* You can **Approve** or **Deny**
* No action occurs without consent

**Key Concept:**
MCP enforces *human-in-the-loop control* for all sensitive operations.

---

## Troubleshooting

If the server does not appear:

* Validate JSON syntax (missing commas are common)
* Ensure absolute paths are used
* Test the server manually:

  ```bash
  npx -y @modelcontextprotocol/server-filesystem /Users/YOUR_USERNAME/Desktop
  ```

---

## Completion Criteria

Participants should be able to confirm:

* [ ] Claude detects the filesystem MCP server
* [ ] File operations require approval
* [ ] Files are created and moved successfully
* [ ] MCP tool usage is visible and understandable

---

## Reflection (Optional Discussion)

* What risks would exist without approval prompts?
* How does this compare to traditional plugins or integrations?
* What other local tools might benefit from MCP?

---
