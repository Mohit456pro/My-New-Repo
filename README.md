# Flask Password Manager

## Project Title and Description
A lightweight, local, in-memory web application that allows you to safely store and retrieve credentials for your accounts without using a complex database. 
It runs on a local web server and provides standard web API endpoints to add, search for, and delete passwords securely and instantly.


## ## Prerequisites
Ensure the following are installed globally on your machine:

**PYTHON**: **VS CODE**: **PYTHON EXTENSION** **FLASK** **GIT BASH**

## Installation and Setup Steps

Follow these step-by-step instructions to download and run the password manager on your own machine:

1. Open the Project in VS Code
   1. Launch VS Code.
   2. Go to **File > Open Folder...** and select your `Flask_Git_Project` folder.
   3. Open the integrated terminal in VS Code: **Terminal > New Terminal** (or press `Ctrl + \``).

2. Set Default Terminal to Command Prompt
   1. In the terminal window, click the dropdown menu next to the `+` sign.
   2. Select **Command Prompt** as your terminal.

3. Select the Global Python Interpreter
   1. Press `Ctrl + Shift + P` to open the Command Palette.
   2. Search for **Python: Select Interpreter** and select it.
  
4. Install dependencies:
   1. **pip install Flask**
---

## Running the Application

To run the Flask application with debug mode enabled, run the following command in your VS Code Git Bash terminal:

```Command Prmpt
python -m flask --app Endpoint_workflow run --debug

Once started, the server will run locally at Bash: `http://127.0.0.1:5000/`

```
## Testing the Endpoints (with Curl in Git Bash)

Open a separate Git Bash terminal or use the existing one to run these `curl` commands and test the application:

1. Test Home Endpoint (GET)
```bash
curl http://127.0.0.1:5000/
```
* **Expected Output:** `Welcome to the App`

2. Test Health Endpoint (GET)
```bash
curl http://127.0.0.1:5000/health
```
* **Expected Output:** `App is running`

3. Add a New User (POST with JSON)
```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "Mohit", "password": "securepassword123"}' http://127.0.0.1:5000/add
```
* **Expected Output:**
  ```json
  {"message":"User added successfully","status":"success"}

4. Delete a User (POST with JSON)
```bash
curl -X DELETE http://127.0.0.1:5000/delete/alex
```
* **Expected Output:**
   ```json
  {
  "message": "User 'alex' deleted successfully","status": "success"}


## API Endpoint Reference

| Endpoint | Method | Behavior | Example Response |
| :--- | :--- | :--- | :--- |
| `/` | `GET` | Returns a friendly landing page greeting. | `"Welcome to the App"` |
| `/health` | `GET` | Displays the server status to verify it is running. | `"App is running"` |
| `/add` | `POST` | Accepts a JSON body containing a username and password and stores it in memory. | `{"status": "success", "message": "User added successfully"}` |
| `/get/<username>` | `GET` | Retrieves the stored password for the given username. Returns a `404` error if the user does not exist. | `{"username": "Mohit", "password": "securepassword123"}` |
| `/delete/<username>` | `DELETE` or `GET` | Removes the specified username and password from storage. Returns a `404` error if the user does not exist. | `{"status": "success", "message": "User 'Mohit' deleted successfully"}` |

---

## Git Workflow

To ensure stability, this project strictly followed professional feature-branch development:

1. **Main Branch (`main`):** Kept as a clean and deployable branch representing live releases. No code was written directly on this branch.
2. **Development Branch (`dev`):** Used as the primary branch for coding and testing new features.
3. **Merging Protocol:** Code was merged from `dev` into `main` only after passing local verification. Merges were performed using `--no-ff` (no-fast-forward) to preserve a clear visual merge bubble and release history.

```
dev:   o---o---o (commits)
            \
main:  o-----o (merge: Version 1)
```

```
dev:        o---o (new commits: add/get + delete)
                 \
main:  o-----o----o (merge: Version 2)
```

---

## Version History

|---------|------------------|

| **Version 1** | Basic Flask app with `/` (welcome message) and `/health` (status check) endpoints |
| **Version 2** | Everything in Version , plus the full password manager: `POST /add` and `GET /get/<username>`, and `GET /delete/<username>` 
---

## Screenshots

### 1. Working Application Endpoint
Below is the root endpoint of the application running locally in the browser:

#### Home Endpoint (/)
Below is the root endpoint of the application running locally in the browser:
![Application running in browser](screenshots/welcome_to_the_app.png)

#### Retrieve Password Endpoint (/get/Mohit)
Below is the response showing retrieved user credentials in JSON format:
![GET User Endpoint](screenshots/Mohit_user.png)

#### Delete a User (delete/alex)
Below is the response showing deleted user successfully in JSON format:
![GET User Endpoint](screenshots/User_deleted_git_bash.png)


### 2. GitHub Branches
The repository branches page showing the active development (`dev`) and stable release (`main`) branches:
![GitHub dev and main branches](screenshots/github_branches.png)

### 3. Commit and Merge History
The repository page showing the files and the successful merge message (`Merge branch 'dev'`):
![GitHub dev and main branches](screenshots/commit_and_merge_history.png)

