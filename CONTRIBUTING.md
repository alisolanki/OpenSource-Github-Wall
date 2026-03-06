# Contributing to OpenSource Github Wall

Follow these steps to add your profile.

---

## Step 0: Communication

Before opening a pull request, open an issue and ask if the repository is active.

---

## Step 1: Fork the Repository

Click the **Fork** button at the top-right of this page and fork the repository to your account.

---

## Step 2: Create a Branch

Create a new branch with this format:

```
add-your-github-username
```

Example:

```
add-john-doe
```

---

## Step 3: Add Your File

Inside the `contributors` folder, create a new file named:

```
your-github-username.json
```

Example:

```
john-doe.json
```

> **Important:** The file name must end with `.json` only — not `.json.txt` or any other extension.

---

## Step 4: File Format

Your file should contain the following fields:

| Field      | Required | Description                     |
|------------|----------|---------------------------------|
| `name`     | ✅ Yes   | Your full name                  |
| `country`  | ✅ Yes   | Your country                    |
| `role`     | ✅ Yes   | Your role (e.g. Developer)      |
| `github`   | ✅ Yes   | Full GitHub URL                 |
| `linkedin` | ❌ No    | Full LinkedIn URL (if you have one) |
| `highlight`| ❌ No    | One short thing you've built or learned |

Example structure:

```json
{
  "name": "Your Name",
  "country": "Your Country",
  "role": "Your Role",
  "github": "https://github.com/yourusername",
  "linkedin": "https://linkedin.com/in/yourprofile",
  "highlight": "One short thing you've built or learned"
}
```

> **Tips:**
> - All field values must be non-empty strings
> - The `github` field must be a full URL starting with `https://github.com/`
> - Omit optional fields entirely if you don't want to include them (do not leave them empty)

---

## Step 5: Commit Your Changes

Commit your file to your branch, not to the main branch.

Commit message:

```
Add my profile to OpenSource Github Wall
```

---

## Step 6: Open a Pull Request

Open a pull request to the main branch.

Title:

```
Add my profile to OpenSource Github Wall
```

Description:

```
Added my contributor JSON file.
```

---

## Rules

- One contributor = one file
- Do not edit other files
- Do not edit README
- Always use a branch
- Keep your pull request clean
- File must be valid JSON — validate it before submitting

Wait for review or merge.
