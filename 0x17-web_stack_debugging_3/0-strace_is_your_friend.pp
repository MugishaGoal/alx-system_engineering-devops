# An automated Puppet manifest to fix the 500 error of a wordpress site

class web_server::fix_wordpress {
  exec { 'fix-wordpress':
    command => '/bin/bash -c "sed -i s/class-wp-locale.phpp/class-wp-locale.php/ /var/www/html/wp-settings.php; /bin/systemctl restart apache2"',
    path    => '/usr/bin:/usr/sbin:/bin',
    onlyif  => '/bin/systemctl is-active apache2 && /bin/systemctl --quiet is-active apache2',
  }
}

class { 'web_server::fix_wordpress': }
