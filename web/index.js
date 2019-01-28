function askDirPath(){
    external.ask_dir_path();
    document.getElementById("finder").disabled = true;
}

function updatePath(targetDirPath) {
    document.getElementById("target-path").textContent = targetDirPath;
    document.getElementById("finder").disabled = false;
}

function confirm() {
    py_confirm(document.getElementById("target-path").textContent)
}