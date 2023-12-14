<?php
// Get query, topk, and engine from the request
$query = $_GET['query'];
$topk = $_GET['topk'];
$engine = $_GET['engine'];

// Set the path to your C binaries
$binaryPath = '.\index-db'; // Sesuaikan dengan path di server Anda

// Run the corresponding back-end code based on the selected engine
if ($engine === 'c-code') {
    // Run your C binary with the appropriate arguments
    // Adjust the command based on your actual C binary and arguments
    $command = $binaryPath . '/querydb ' . escapeshellarg($query) . ' ' . escapeshellarg($topk);
    exec($command, $output, $returnCode);

    // Check if the execution was successful
    if ($returnCode === 0) {
        // Parse the output (assuming it's in a specific format)
        $results = parseCOutput($output);

        // Return results as JSON
        header('Content-Type: application/json');
        echo json_encode($results);
    } else {
        // Handle the error
        header('HTTP/1.1 500 Internal Server Error');
        echo json_encode(['error' => 'Failed to execute the C binary']);
    }
} else {
    // Handle other engines if needed
    header('HTTP/1.1 400 Bad Request');
    echo json_encode(['error' => 'Invalid engine']);
}

// Function to parse the C binary output (adjust based on your output format)
function parseCOutput($output) {
    $results = [];

    // Implement the parsing logic based on your C binary output format
    // Example: assuming each line is in the format "doc_id score"
    foreach ($output as $line) {
        list($docId, $score) = explode(' ', $line);
        $results[] = ['doc_id' => (int)$docId, 'score' => (float)$score];
    }

    return $results;
}
?>
