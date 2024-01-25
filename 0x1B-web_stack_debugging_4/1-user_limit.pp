# Change the OS configuration so that it is possible to login with holberton

exec { 'Allows-holberton-user-to login':
  command => "sed -iE 's/^holberton hard nofile \
.*/holberton hard nofile 88888/' /etc/security/limits.conf && \
sed -iE 's/^holberton soft nofile .*/holberton soft nofile 88888/' \
/etc/security/limits.conf",
  path    => '/usr/bin:/usr/sbin:/bin',
}
