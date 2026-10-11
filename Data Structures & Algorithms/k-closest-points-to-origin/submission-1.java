// import java.util.PriorityQueue;

class Point {
    int x;
    int y;
    long distSq;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
        this.distSq = (long) x * x + (long) y * y;
    }
}

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<Point> maxHeap = new PriorityQueue<>(
            (a, b) -> Long.compare(b.distSq, a.distSq)
        );

        for (int[] pt : points) {
            maxHeap.offer(new Point(pt[0], pt[1]));
            if (maxHeap.size() > k) {
                maxHeap.poll();
            }
        }

        int[][] result = new int[k][2];
        int idx = 0;
        while (!maxHeap.isEmpty()) {
            Point p = maxHeap.poll();
            result[idx][0] = p.x;
            result[idx][1] = p.y;
            idx++;
        }

        return result;
    }
}