#!/bin/bash

missing_args() {
  echo "Error: option requires an argument -- $1" 1>&2
  exit 1
}

for opt in "$@"; do
  case "$opt" in
    '--owner' )
      if [[ -z "$2" ]] || [[ "$2" =~ ^-+ ]]; then
        missing_args $opt
      fi
      owner="$2"
      shift 2
      ;;
    '--repository' )
      if [[ -z "$2" ]] || [[ "$2" =~ ^-+ ]]; then
        missing_args $opt
      fi
      repository="$2"
      shift 2
      ;;
    '--branch' )
      if [[ -z "$2" ]] || [[ "$2" =~ ^-+ ]]; then
        missing_args $opt
      fi
      branch="$2"
      shift 2
      ;;
  esac
done

git clone https://github.com/${owner}/${repository}
cd ${repository}/
git checkout $branch
cd apps/
python manage.py runserver 0.0.0.0:8000
