# Creates a custom HTTP header response, but with Puppet.
# Ensure Nginx is installed
class { 'nginx':
  ensure => 'installed',
}

# Custom fact to get the hostname
Facter.add('custom_hostname') do
  setcode 'hostname'
end

# Configure Nginx with custom HTTP header
file { '/etc/nginx/sites-available/custom-header':
  content => "add_header X-Served-By $custom_hostname;",
}

file { '/etc/nginx/sites-enabled/000-default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/custom-header',
}

file { '/etc/nginx/sites-enabled/default':
  ensure => 'absent',
}

# Restart Nginx to apply changes
service { 'nginx':
  ensure  => 'running',
  require => File['/etc/nginx/sites-available/custom-header'],
}

# Notify user about the need to restart Nginx manually
notify { 'restart_nginx_manually':
  message => 'Please restart Nginx manually to apply the changes: sudo service nginx restart',
  require => Service['nginx'],
}
