# Notes on deploying art-dash

## mariadb

The backing storage is mariadb, with a persistent volume and some enhancement
to enable secure ingress from buildvm (outside the cluster).

### Secrets

```bash
dir=deploy/secrets

# extract existing copy of the secret
oc login ...
oc project ...
for secret in mariadb{,-secure}; do
  mkdir $dir/$secret
  oc extract secret/$secret --to $dir/$secret
done

# use that, or contents from our vault in a dir, to re-create
oc login ...
oc project ...
for secret in mariadb{,-secure}; do
  oc create secret generic $secret --from-file $dir/$secret
done
```

**`mariadb`** contains the passwords and such for the DB itself.

* `database-user`
* `database-name`
* `database-password`
* `database-root-password`

**`mariadb-secure`** contains the configuration for setting up stunnel to run
alongside mariadb, accepting an HTTPS connection and decrypting it to pass on
to mariadb.

* `ca.pem`: CA for the client to validate the server
* `ca-key.pem`: key for generating certs against that CA (not needed here)
* `server-cert-chain.pem`: chain from CA to server
* `server-cert.pem`: stunnel server cert
* `server-key.pem`: stunnel server key
* `stunnel-client.conf`: stunnel client conf (only needed on buildvm)
* `stunnel-server.conf`: conf for running the stunnel service here

### Deployment

Login to the server (ocp4.psi) and select the appropriate project (aos-art-web). Then:

    oc create -f deploy/mariadb.yaml

## art-dash-server

This is a python Django project to provide the backend of the app, based on this repo.

### Secrets


```bash
dir=deploy/secrets

# extract existing copy of the secret
oc login ...
oc project ...
for secret in errata-keytab art-dash-server-configs; do
  mkdir $dir/$secret
  oc extract secret/$secret --to $dir/$secret
done

# use that, or contents from our vault in a dir, to re-create
oc login ...
oc project ...
for secret in errata-keytab art-dash-server-configs; do
  oc create secret generic $secret --from-file $dir/$secret
done
```

**`errata-keytab`** contains the read-only kerberos keytab for reading errata information

**`art-dash-server-configs`** contains server secrets

### Deployment

Login to the server (ocp4.psi) and select the appropriate project (aos-art-web). Then:

    oc create -f deploy/art-dash-server.yaml

