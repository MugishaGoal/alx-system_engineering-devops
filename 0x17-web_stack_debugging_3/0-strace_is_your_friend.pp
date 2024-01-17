# An automated Puppet manifest to fix the 500 error of a wordpress site

exec { 'fixing-manifest':
  command => 'bash -c "sed -i s/class-wp-locale.phpp/class-wp-locale.php/  \
              /var/www/html/wp-settings.php; service apache2 restart"',
  path    => '/usr/bin:/usr/sbin:/bin'
}
