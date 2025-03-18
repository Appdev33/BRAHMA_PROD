import java.util.*;

class Ideone {
    public static void main(String[] args) {
        List<List<String>> input = Arrays.asList(
            Arrays.asList("A", "B"),
            Arrays.asList("C", "D"),
            Arrays.asList("B", "D"),
            Arrays.asList("C", "E"),
            Arrays.asList("E", "A")
        );

        // Directed graph stored as adjacency list
        HashMap<String, List<String>> graph = new HashMap<>();
        HashMap<String, Boolean> visited = new HashMap<>();

        // Build the graph
        for (List<String> edge : input) {
            String from = edge.get(0);
            String to = edge.get(1);
            graph.computeIfAbsent(from, k -> new ArrayList<>()).add(to);
            graph.putIfAbsent(to, new ArrayList<>()); // Ensure all nodes are in the graph
        }

        int longestPathLength = 0;
        List<String> longestPath = new ArrayList<>();

        // Find the longest path
        for (String node : graph.keySet()) {
            List<String> currentPath = new ArrayList<>();
            int currentLength = dfs(node, graph, visited, currentPath);
            if (currentLength > longestPathLength) {
                longestPathLength = currentLength;
                longestPath = new ArrayList<>(currentPath);
            }
        }

        System.out.println("Longest Path Length (edges): " + longestPathLength);
        System.out.println("Longest Path: " + longestPath);
    }

    public static int dfs(String node, HashMap<String, List<String>> graph, HashMap<String, Boolean> visited, List<String> currentPath) {
        if (visited.getOrDefault(node, false)) {
            return 0; // Avoid cycles in directed graph
        }

        visited.put(node, true);
        currentPath.add(node);

        int maxLength = 0;
        List<String> tempPath = new ArrayList<>();

        for (String neighbor : graph.get(node)) {
            List<String> neighborPath = new ArrayList<>();
            int length = dfs(neighbor, graph, visited, neighborPath);
            if (length > maxLength) {
                maxLength = length;
                tempPath = new ArrayList<>(neighborPath);
            }
        }

        currentPath.addAll(tempPath);
        visited.put(node, false); // Backtracking

        return 1 + maxLength; // Add 1 for the current node
    }
}
