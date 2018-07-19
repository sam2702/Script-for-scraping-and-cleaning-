import path
import sh

for project in path.Path(".").dirs():
    with project:
        sh.git.clean(force=True)
        sh.git.reset(hard=True)
        sh.make()
