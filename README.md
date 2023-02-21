# Nick's dotfiles

## Install chezmoi

### Mac

```
brew install chezmoi
```

### Linux

- Arch

  ```
  pacman -S chezmoi
  ```

### One line binary install

```
sh -c "$(curl -fsLS get.chezmoi.io)"
```

[Reference](https://www.chezmoi.io/install/#one-line-package-install)

## Init new env

```
chezmoi init --apply --verbose https://github.com/npenkov/dotfiles.git
```

if the decryption fails - use:

```sh
age --decrypt --output "${HOME}/key.txt" "$HOME/.local/share/chezmoi/key.txt.age"
```
