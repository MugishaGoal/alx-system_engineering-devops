# 7-puppet_install_nginx_web_server.pp
# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Create an index.html file with "Hello World" content
file { '/var/www/html/index.html':
  content => 'Hello World',
}

# Configure a 301 redirect in the Nginx default configuration
file_line { 'redirection-301':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

# Ensure that the Nginx service is running
service { 'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}
