package test;




import io.grpc.Grpc;
import io.grpc.InsecureServerCredentials;
import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.stub.StreamObserver;
import java.io.IOException;
import java.util.concurrent.TimeUnit;
import java.util.logging.Logger;

/**
 * A sample gRPC server
 */
public class ProtoServer {
    private static final Logger logger = Logger.getLogger(ProtoServer.class.getName());

    private final int port;
    private final Server server;


    /** Create a RouteGuide server using serverBuilder as a base and features as data. */
    public ProtoServer(int port) {
        this.port = port;
        ServerBuilder<?> serverBuilder = Grpc.newServerBuilderForPort(port, InsecureServerCredentials.create());
        server = serverBuilder.addService(new OrdersService())
                .build();
    }

    /** Start serving requests. */
    public void start() throws IOException {
        server.start();
        logger.info("Server started, listening on " + port);
        Runtime.getRuntime().addShutdownHook(new Thread() {
            @Override
            public void run() {
                // Use stderr here since the logger may have been reset by its JVM shutdown hook.
                System.err.println("*** shutting down gRPC server since JVM is shutting down");
                try {
                    ProtoServer.this.stop();
                } catch (InterruptedException e) {
                    e.printStackTrace(System.err);
                }
                System.err.println("*** server shut down");
            }
        });
    }

    /** Stop serving requests and shutdown resources. */
    public void stop() throws InterruptedException {
        if (server != null) {
            server.shutdown().awaitTermination(30, TimeUnit.SECONDS);
        }
    }

    /**
     * Await termination on the main thread since the grpc library uses daemon threads.
     */
    private void blockUntilShutdown() throws InterruptedException {
        if (server != null) {
            server.awaitTermination();
        }
    }

    /**
     * Main method.  This comment makes the linter happy.
     */
    public static void main(String[] args) throws Exception {
        ProtoServer server = new ProtoServer(8980);
        server.start();
        server.blockUntilShutdown();
    }

    /**
     * Our implementation of RouteGuide service.
     *
     * <p>See route_guide.proto for details of the methods.
     */
    private static class OrdersService extends OrdersGrpc.OrdersImplBase {


        OrdersService() {

        }


        public void getOrders(OrdersOuterClass.OrderRequest request, StreamObserver<OrdersOuterClass.OrderResponse> responseObserver)
        {
            OrdersOuterClass.Order order = OrdersOuterClass.Order.newBuilder().setCol1(1).build();
            responseObserver.onNext(OrdersOuterClass.OrderResponse.newBuilder().addOrders(order).build());
            responseObserver.onCompleted();

        }


        public void getOrdersStream(OrdersOuterClass.OrderRequest request, StreamObserver<OrdersOuterClass.Order> responseObserver)
        {
            responseObserver.onCompleted();
        }

    }
}
