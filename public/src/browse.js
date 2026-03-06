let currentPath = []; 
let selectedFile = null;

function init() {
    navigateTo(rootData, "Project");
}

function navigateTo(folderData, folderName) {
    // Manage Path History
    const existingIndex = currentPath.findIndex(p => p.name === folderName);
    if (existingIndex !== -1) {
        currentPath = currentPath.slice(0, existingIndex + 1);
    } else {
        currentPath.push({ name: folderName, data: folderData });
    }
    // 2. Clear current selection (since we are moving to a new folder)
    selectedFileName = null;
    selectedFile = null;

    // 3. Redraw UI
    renderBreadcrumbs();
    renderFileList(folderData);
    
    // 4. THE FIX: Refresh the footer count and selection text
    updateFooterStatus();
    renderBreadcrumbs();
}

// Change this number to control how many folders show before collapsing
const MAX_VISIBLE_BREADCRUMBS = 3;

function renderBreadcrumbs() {
    const container = document.getElementById('breadcrumb-container');
    const moreBtn = document.getElementById('breadcrumb-more');
    const moreMenu = document.getElementById('more-menu');
    const moreSep = document.querySelector('.more-sep');
    
    container.innerHTML = '';
    moreMenu.innerHTML = '';

    if (currentPath.length <= MAX_VISIBLE_BREADCRUMBS) {
        // Standard view: No "..."
        moreBtn.classList.add('hidden');
        moreSep.classList.add('hidden');
        renderItems(currentPath, container);
    } else {
        // Truncated view
        moreBtn.classList.remove('hidden');
        moreSep.classList.remove('hidden');

        // Split the path: Hidden vs Visible
        const hiddenItems = currentPath.slice(0, currentPath.length - (MAX_VISIBLE_BREADCRUMBS - 1));
        const visibleItems = currentPath.slice(currentPath.length - (MAX_VISIBLE_BREADCRUMBS - 1));
        console.log(hiddenItems)
        // Fill the "..." Menu
        hiddenItems.forEach(step => {
            const item = document.createElement('div');
            item.className = 'menu-item';
            item.textContent = step.name;
            item.onclick = () => navigateTo(step.data, step.name);
            moreMenu.appendChild(item);
        });

        // Fill the visible area
        renderItems(visibleItems, container);
    }
}

// Helper to render segments with separators
function renderItems(items, targetContainer) {
    items.forEach((step, index) => {
        const span = document.createElement('span');
        span.className = 'breadcrumb-item';
        span.textContent = step.name;
        span.onclick = () => navigateTo(step.data, step.name);
        targetContainer.appendChild(span);

        if (index < items.length - 1) {
            const sep = document.createElement('span');
            sep.className = 'breadcrumb-separator';
            sep.textContent = '>';
            targetContainer.appendChild(sep);
        }
    });
}

function renderFileList(data) {
    const container = document.getElementById('file-list');
    container.innerHTML = '';

    data.forEach(item => {
        const row = document.createElement('div');
        row.className = 'tree-node';
        row.title = item.name; // Tooltip on hover

        const icon = document.createElement('i');
        icon.className = item.type === 'folder' ? 'bi bi-folder-fill me-2' : 'bi bi-file-earmark me-2';
        icon.style.color = item.type === 'folder' ? '#E95420' : '#6c757d';
        icon.style.marginRight = "10px";

        const text = document.createElement('span');
        text.className = 'file-label';
        text.textContent = item.name;

        row.appendChild(icon);
        row.appendChild(text);

        // Update the click handler inside renderFileList:
        row.onclick = () => {
            if (item.type === 'folder') {
                selectedFileName = null; // Clear selection when entering a new folder
                navigateTo(item.children, item.name);
            } else {
                if (selectedFile) selectedFile.classList.remove('selected-file');
                row.classList.add('selected-file');
                selectedFile = row;
                selectedFileName = item.name;
                
                // Refresh footer to show selection
                updateFooterStatus(data); 
            }
        };
        container.appendChild(row);
    });
}

export function filterFiles() {
    const input = document.getElementById('file-search').value;
    const rows = document.querySelectorAll('.tree-node');

    if (!input) {
        rows.forEach(row => row.style.display = 'flex');
        return;
    }

    // 1. Convert glob pattern to Regex
    // Escape special characters (like . or +) except for our '*'
    let pattern = input.replace(/[.+^${}()|[\]\\]/g, '\\$&'); 
    
    // Replace '*' with '.*' (the regex wildcard)
    pattern = pattern.replace(/\*/g, '.*');

    // Create the regex. '^' ensures it matches from the START of the filename
    try {
        const regex = new RegExp('^' + pattern, 'i'); // 'i' for case-insensitive

        rows.forEach(row => {
            const fileName = row.querySelector('.file-label').textContent;
            // 2. Test the filename against the pattern
            row.style.display = regex.test(fileName) ? 'flex' : 'none';
        });
    } catch (e) {
        // If the user types an invalid partial regex, we fail gracefully
        console.error("Invalid search pattern");
    }

    // 4. THE FIX: Refresh the footer count and selection text
    updateFooterStatus();
}

let selectedFileName = null; // Store the currently selected file

function updateFooterStatus() {
    const folderInfo = document.getElementById('folder-info');
    const selectionInfo = document.getElementById('selection-info');
    const openBtn = document.getElementById('open-btn');
    
    // 1. Calculate Folder Stats (Filtered items)
    const visibleRows = Array.from(document.querySelectorAll('.tree-node'))
                             .filter(row => row.style.display !== 'none');
    const count = visibleRows.length;
    folderInfo.textContent = count === 1 ? "1 item" : `${count} items`;

    // 2. Update Selection Info
    if (selectedFileName) {
        selectionInfo.textContent = selectedFileName;
        openBtn.disabled = false;
    } else {
        selectionInfo.textContent = ""; // Keep empty if no file picked
        openBtn.disabled = true;
    }
}


export function handleOpen() {
    if (selectedFileName) {
        // 1. Get folder names from currentPath (e.g., ["Project", "src", "js"])
        const pathSegments = currentPath.map(step => step.name);
        
        // 2. Combine with the selected file name
        pathSegments.push(selectedFileName);
        
        // 3. Join with "/" to create the absolute path
        const absolutePath = "/" + pathSegments.join("/");
        
        console.log("Absolute Path:", absolutePath);
        
        // You can return this to your main application or close the popup
        alert("Selected: " + absolutePath);
        togglePopup();
    }
}

export function togglePopup() {
    const popup = document.getElementById('file-popup');
    const isVisible = popup.style.display === 'flex';
    popup.style.display = isVisible ? 'none' : 'flex';
    if (!isVisible) init(); // Load root on open
}

