Title: Git versus Mercurial
Date: 2013-05-04 18:17
Author: Tony
Slug: git-versus-mercurial
Status: published

I know very little about the religious war of Git versus Mercurial, but ignorance has never stopped me from having a firm opinion.  
  
I come down on the side of Git for these reasons:  

#### Local Version Numbers

Mercurial has the idea of local version numbers as well as universal hashes. I don't like these extra local version numbers because it's an additional feature that muddies the waters without really contributing anything. Git uses hashes that are universal. You can specify versions locally in an easy way using the tilde notation.  

#### Approach To History

Okay, local version numbers is just an annoyance. The big difference for me is that for Mercurial, history is literal, but for Git, history is a story. If you ask someone what they did yesterday evening, they'll say something like, "I watched Holby City", they don't say "I sat on the bean bag next to the sofa at 20:00 and put the TV on and changed the channel to BBC1 and then watched the screen for approximately 1 hour...". The first is the Git answer, where you summarize the salient points after they occur. The second is the Mercurial approach where you give a verbatim replay of the events as they occurred. So with Git you're encouraged to tidy up your history before you push to a public repository. With Mercurial you're encouraged to view history as immutable, and however you got to the point you're at, that's what you make public.  

#### Indiscriminate Push

With Git you get to explicitly push individual branches to a remote repository. With Mercurial, the push command pushes all branches to the remote repository, which isn't necessarily what you want. Mercurial tries to get round this with bookmarks, but I feel that this is a hack, and that Git's branches are more elegant. With Mercurial, branches are part of the commit, but with Git, branches are references held outside the commit. The Git approach turns out to be the way to go.  
