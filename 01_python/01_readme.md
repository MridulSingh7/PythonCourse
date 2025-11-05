always work in virtual environment, its a good practise and it doesnt affect another code
to do so
1. open the folder you want to create a virtual environment for in integrated terminal , type [ python3 -m venv .venv ] or python -m venv .venv (venv and .venv same)
2. do the command = . .venv/bin/activate to activate the virtual environment
3. you have a requirements.txt file, which is same as package.json
4. to install dependencies pip install -r requirements.txt , this will install all the dependencies mentioned in the requirements.txt file
5. we can exit virtual environment by running deactivate in terminal



############ WHY DO WE NEED THAT?
if we need to install modules, work with third party softwares, its a good practise to work in virtual environment
1. Necessity of Virtual Environments: Virtual environments prevent issues that arise when multiple projects require different versions of the same library. An analogy is used to illustrate how these conflicts can occur.

2. Creating Virtual Environments: The lecture provides a step-by-step guide on using Python's built-in venv module to create a virtual environment, including setting up a folder, activating it, and installing libraries like Flask.

3. Managing Dependencies: The importance of a requirements.txt file is emphasized, which allows for easy sharing and replication of the project’s environment.

4. Best Practice: Working within a virtual environment is recommended to ensure portability and prevent compatibility issues across different systems.

5. Future Tools: The speaker hints at introducing a newer tool called uv for managing virtual environments, which promises a more streamlined experience in upcoming sessions.



//what is pep8?
pep8 ensures that python code is written in a readable and consistent format across the community, its official style guide for python
//how to import zen of python?  in terminal : "import this"