# demo of RemoveSelection

# Done!

# match 'login', :to => 'account#login'
# match 'logout', :to => 'account#logout'

# this line will be removed from cursors
match 'account/register', :to => 'account#register'

# match 'account/lost_password', :to => 'account#lost_password'

# this too
match 'account/activate', :to => 'account#activate'

# match '/news/preview', :controller => 'previews', :action => 'news'
# match '/issues/preview/new/:project_id', :to => 'previews#issue'
# match '/issues/preview/edit/:id', :to => 'previews#issue'

# and this
match '/issues/preview', :to => 'previews#issue'