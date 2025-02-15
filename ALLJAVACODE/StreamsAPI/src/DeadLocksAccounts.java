import java.util.Random;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class DeadLocksAccounts {

	public class Runner {
		private Account acc1 = new Account();
		private Account acc2 = new Account();

		private Lock lock1 = new ReentrantLock();
		private Lock lock2 = new ReentrantLock();

		// Solution --> To DeadLock
		private void acquireLocks(Lock lock1, Lock lock2) throws InterruptedException {
			while (true) {
				// Acquire Lock
				Boolean gotFirstLock = false;
				Boolean gotSecondLock = false;

				try {
					gotFirstLock = lock1.tryLock(); // Return true if have
					gotSecondLock = lock2.tryLock();
				} finally {
					if (gotFirstLock && gotSecondLock) {
						return;
					}

					if (gotFirstLock) {
						lock1.unlock();
					}

					if (gotSecondLock) {
						lock2.unlock();
					}
				}

				// Lock not acquired
				Thread.sleep(1);
			}
		}

		public void firstThread() throws InterruptedException {
			Random random = new Random();

			for (int i = 0; i < 200000; i++) {
				acquireLocks(lock1, lock2);
				try {
					Account.transfer(acc1, acc2, random.nextInt(100)); // Transfer range(0-99)
				} finally {
					lock1.unlock();
					lock2.unlock();
				}
			}
		}// EndOf firstThread()

		public void secondThread() throws InterruptedException {
			Random random = new Random();

			for (int i = 0; i < 200000; i++) {
				System.out.println("Making transactions "+ (i+1));
				/*
				 * Dead Lock (Did not lock in the same Order)
				 * 
				 * lock2.lock(); lock1.lock();
				 */
				acquireLocks(lock2, lock1);
				try {
					Account.transfer(acc2, acc1, random.nextInt(100)); // Transfer range(0-99)
				} finally {
					lock1.unlock();
					lock2.unlock();
				}
			}
		}// EndOf secondThread()

		public void finished() {
			System.out.println("Account 1 Balance: " + acc1.getBalance());
			System.out.println("Account 2 Balance: " + acc2.getBalance());
			System.out.println("Total Account Balance: " + (acc1.getBalance() + acc2.getBalance()));
		}// EndOf Finished()
	}

	public class Account {
		private int balance = 1000;

		public void deposit(int amount) {
			balance += amount;
		}

		public void withdraw(int amount) {
			balance -= amount;
		}

		public int getBalance() {
			return balance;
		}

		public static void transfer(Account acc1, Account acc2, int amount) {
			acc1.withdraw(amount);
			acc2.deposit(amount);
		}
	}

	public static void main(String[] args) throws InterruptedException {
		DeadLocksAccounts obj = new DeadLocksAccounts();
		final DeadLocksAccounts.Runner runner = obj.new Runner();
		Thread t1 = new Thread(new Runnable() {

			@Override
			public void run() {
				try {
					runner.firstThread();
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}

		});

		Thread t2 = new Thread(new Runnable() {

			@Override
			public void run() {
				try {
					runner.secondThread();
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}

		});

		// Start
		t1.start();
		t2.start();

		t1.join();
		t2.join();

		runner.finished();
	}// ENDof Main

}


/*
 This code simulates a scenario where two threads are transferring money between two bank accounts (acc1 and acc2). 
 The Runner class orchestrates these transfers using two locks (lock1 and lock2) to avoid potential deadlocks.

Here's a breakdown of the code:

Runner Class:
Instance Variables:

acc1 and acc2: Instances of the Account class representing two bank accounts.
lock1 and lock2: Instances of ReentrantLock used as locks for synchronization.

acquireLocks Method:
Acquires locks lock1 and lock2 simultaneously in a way that prevents deadlocks.
It tries to acquire both locks in a loop. If both locks are acquired successfully, it returns; otherwise, it releases any 
locks that were acquired and waits for a short period before trying again.

firstThread Method:
Simulates one thread transferring money from acc1 to acc2.
It acquires locks in the same order (lock1 and then lock2) as the transfer method in the Account class to prevent deadlocks.
Performs 1000 transfers using the transfer method and random amounts.

secondThread Method:
Simulates another thread transferring money from acc2 to acc1.
Unlike the firstThread, it acquires locks in the opposite order (lock2 and then lock1).
This difference in lock acquisition order demonstrates a potential deadlock scenario, which is addressed by the acquireLocks method.

finished Method:
Prints the balances of both accounts and the total balance.
Account Class:
Instance Variables:

balance: Represents the current balance of the account.

Methods:
deposit: Increases the account balance by the specified amount.
withdraw: Decreases the account balance by the specified amount.
getBalance: Returns the current balance of the account.
transfer: Static method that transfers money from one account to another. It involves withdrawing the specified amount from one account and depositing it into the other.
Deadlock Mitigation:
The deadlock is mitigated by ensuring that both threads acquire locks in the same order (lock1 followed by lock2). 
This prevents a scenario where one thread holds one lock while waiting for the other lock, while the other thread holds the second lock and waits for the first, 
leading to a deadlock.
Overall, this code illustrates the importance of careful lock acquisition order to avoid potential deadlocks in multithreaded applications.
*/


/*
 * In the provided code, the intentional acquisition of locks in opposite orders in the secondThread method is done to illustrate a potential 
 * scenario where a deadlock might occur. Deadlocks happen when two or more threads are blocked forever, each waiting for the other to release a lock. Here's how the deadlock can occur in this specific example:

Scenario without Mitigation (Acquiring Locks in Opposite Orders):
firstThread Method:

Acquires lock1.
Attempts to acquire lock2.
secondThread Method:

Acquires lock2.
Attempts to acquire lock1.
If these threads execute concurrently and both reach the point of attempting to acquire the second lock while holding the first, a deadlock can occur.
 Each thread holds a lock that the other thread needs to proceed, resulting in a situation where neither can make progress, and the program becomes stuck.

Mitigation (Acquiring Locks in the Same Order):
To mitigate the potential deadlock, the acquireLocks method is introduced. It attempts to acquire both locks in a specific order (lock1 first, then lock2). 
This ensures that both threads (firstThread and secondThread) acquire locks in the same order during their respective operations. The acquireLocks method checks
 if both locks can be acquired. If they can, it returns; otherwise, it releases any locks that were acquired, and the threads try again.

By acquiring locks in the same order in both threads, the potential for a deadlock is eliminated. Deadlocks occur when threads acquire locks in different orders, 
leading to a circular wait scenario.

The intentional demonstration of deadlock in this code serves as an educational example to highlight the importance of careful lock acquisition order in 
preventing deadlocks. In real-world scenarios, it's crucial to design multithreaded applications with a clear understanding of lock acquisition orders 
to avoid such issues.
*/


