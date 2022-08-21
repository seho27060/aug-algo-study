package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ24446 {
    private static List<Integer> []arr;
    private static int N, M, R;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        arr = new ArrayList[N+1];
        for (int i=0; i<=N; i++) {
            arr[i] = new ArrayList<>();
        }
        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            arr[u].add(v);
            arr[v].add(u);
        }
        bfs(R);
    }

    private static void bfs(int x){
        Queue<Integer> q = new LinkedList<>();
        q.add(x);

        boolean []visited = new boolean[N+1];
        visited[x] = true;

        int []ans = new int[N+1];
        for (int i=1; i<=N; i++){
            ans[i] = -1;
        }
        int depth = 0;
        while (!q.isEmpty()) {
            int s = q.size();
            while (s-- > 0) {
                int t = q.poll();
                ans[t] = depth;
                int s2 = arr[t].size();
                for (int i=0; i<s2; i++) {
                    if (!visited[arr[t].get(i)]) {
                        visited[arr[t].get(i)] = true;
                        q.add(arr[t].get(i));
                    }
                }
            }
            depth++;
        }
        for (int i=1; i<=N; i++) {
            System.out.println(ans[i]);
        }
    }
}