# Handles the servers issue of not handling multiple requests at a time

exec { 'fix-nginx':
  command => "bash -c \"sed -iE 's/^ULIMIT=.*/ULIMIT=\\\"-n 8192\\\"/' \
/etc/default/nginx; service nginx restart\"",
  path    => '/usr/bin:/usr/sbin:/bin'
}
