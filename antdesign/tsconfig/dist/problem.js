var width;
width = getWidth();
if (width === undefined) {
    // ...
}
else if (width === null) {
    // ...
}
else {
    // ...
}
function getWidth() {
    if (Math.random() > 0.3) {
        return undefined;
    }
    else if (Math.random() > 0.6) {
        return null;
    }
    return 0;
}
