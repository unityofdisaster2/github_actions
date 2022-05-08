from git import Repo



def remove_branches_with_prefix(route, prefix):
	repo_ref = Repo(route)
	for branch in repo_ref.branches:
		if branch.name.startswith(prefix):
			repo_ref.git.branch('-D', branch.name)



if __name__ == "__main__":
	base_dir = input('base_dir: ')
	prefix = input('branch prefix: ')
	remove_branches_with_prefix(base_dir, prefix)
