## Setup

You need your own version of this repository, where you can actually change the content as much as you like (and which is not bound to me).

### git setup for the Captain

The captain (and only them) need to execute the following steps:
 
1. Create a new repository in GitHub under your account.
   Choose a meaningful name and description, else you can keep the repository completely empty - we will import some content next.
1. Clone the template repository: `$ git clone https://github.com/felixhekhorn/topi-git-template.git`
1. Change the origin (i.e. the source of truth) of the repository to your personal repo: `$ git remote set-url --all origin https://github.com/<your-account>/<your-repo>.git`
1. Push the current state to _your_ repository: `$ git push`
1. Add the other team members as Collaborators in GitHub to your repo: Security -> Collaborators -> Add people

### git setup for the others

Then everybody needs to clone _the Captain's_ repository: `$ git clone https://github.com/<captain-account>/<captain-repo>.git`

### Use branches and Pull Requests

When a group implements a new feature always create a new branch, e.g. via `$ git switch -c my-new-branch`.
Remember that there will be three groups changing the repository in parallel - you can solve this by using branches.
Don't put too many changes into a single branch, before asking to merge it to the main branch.
Try to make one consistent change, e.g. adding one specific new feature, into one branch.
When you believe your feature is ready, create a Pull Request and ask for a review by the CEO group
(and the CEO group should ask to one or both other groups for their Pull Requests respectively).

Maybe add an intentional bug in your first Pull Request, to check if the Reviewer is actually doing
its job. One time is sufficient, because the material is complex enough that there will be
unintentional bugs around :see_no_evil: .

### Python setup

1. Before you start to develop Python code, make a new virtual environment, e.g. with `$ python -m venv env`.
   This will create a folder `env/` where the actual environment is hosted.
1. Next, you need to activate the new environment via `$ . env/bin/activate`.
   This new environment makes the development independent from the host system, gives full control over
   library versions and better reproducibility.
1. Next, we can install the necessary third-party libraries using `$ pip install -r requirements.txt`
