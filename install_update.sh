#!/bin/bash

# Rendre le script exécutable (pour plus de discrétion)
chmod +x "$0"

# Fonction pour appliquer un thème de couleur avec dconf
change_terminal_theme() {
    # Couleurs en Hexadecimal extraites de votre JSON
    local BACKGROUND_COLOR="#e5ff8f"
    local FOREGROUND_COLOR="#354000"
    local CURSOR_COLOR="#627400"

    local BLACK_COLOR="#d1f600"
    local RED_COLOR="#ffc9d8"
    local GREEN_COLOR="#caed00"
    local YELLOW_COLOR="#ffd0aa"
    local BLUE_COLOR="#b7e0ff"
    local MAGENTA_COLOR="#e0d1ff"
    local CYAN_COLOR="#01fcde"
    local WHITE_COLOR="#627400"

    local BRIGHT_BLACK_COLOR="#9eba00"
    local BRIGHT_RED_COLOR="#ffebf0"
    local BRIGHT_GREEN_COLOR="#e5ff8f"
    local BRIGHT_YELLOW_COLOR="#ffeddf"
    local BRIGHT_BLUE_COLOR="#e4f3ff"
    local BRIGHT_MAGENTA_COLOR="#f3eeff"
    local BRIGHT_CYAN_COLOR="#c5fff2"
    local BRIGHT_WHITE_COLOR="#1f2600"

    # Utilisation de dconf pour appliquer les couleurs au profil par défaut de GNOME Terminal
    dconf write /org/gnome/terminal/legacy/profiles:/default/background-color "'$BACKGROUND_COLOR'"
    dconf write /org/gnome/terminal/legacy/profiles:/default/foreground-color "'$FOREGROUND_COLOR'"
    dconf write /org/gnome/terminal/legacy/profiles:/default/cursor-color "'$CURSOR_COLOR'"

    # Appliquer les couleurs de la palette
    dconf write /org/gnome/terminal/legacy/profiles:/default/palette "['$BLACK_COLOR', '$RED_COLOR', '$GREEN_COLOR', '$YELLOW_COLOR', '$BLUE_COLOR', '$MAGENTA_COLOR', '$CYAN_COLOR', '$WHITE_COLOR', '$BRIGHT_BLACK_COLOR', '$BRIGHT_RED_COLOR', '$BRIGHT_GREEN_COLOR', '$BRIGHT_YELLOW_COLOR', '$BRIGHT_BLUE_COLOR', '$BRIGHT_MAGENTA_COLOR', '$BRIGHT_CYAN_COLOR', '$BRIGHT_WHITE_COLOR']"

    echo "Booo Johnson, fallait être meilleur et ne pas laisser la session ouverte"
}

# Appel de la fonction pour appliquer le thème
change_terminal_theme
