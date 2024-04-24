#!/usr/bin/env puppet
# Installl a specified version of flask (2.1.0)
Package { 'flask':
  ensure => '2.1.0',
  provider => 'pip',

}
